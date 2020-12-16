import json

from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render

from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.edit import FormMixin, UpdateView, DeleteView


from accounts.models import User
from posts.decorator import post_ownership_required
from posts.forms import PostCreationForm
from posts.models import Post, PostImage


HAS_OWNERSHIP = [post_ownership_required, login_required]


class PostListView(ListView):
    queryset = Post.objects.all().annotate(comment_count=Count('comment')).select_related().order_by('-created_at')
    context_object_name = 'post_list'
    paginate_by = 5
    template_name = 'posts/list.html'


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class PostCreateView(CreateView):
    model = Post
    form_class = PostCreationForm
    template_name = 'posts/create.html'

    def form_valid(self, form):
        new_post = form.save(commit=False)
        new_post.author = self.request.user
        new_post.save()

        # 이 방식이 좀 맘에 안듬.. 한번에 save하는 방식을 찾아보자자
        if self.request.FILES.getlist('images'):
            for image in self.request.FILES.getlist('images'):
                new_post_image = PostImage()
                new_post_image.target_post = new_post
                new_post_image.image = image
                new_post_image.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('posts:list')


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'target_post'
    template_name = 'posts/detail.html'



@method_decorator(HAS_OWNERSHIP, 'get')
@method_decorator(HAS_OWNERSHIP, 'post')
class PostUpdateView(UpdateView):
    model = Post
    form_class = PostCreationForm

    def get_success_url(self):  # 이게 왜 안되는지 알아보자
        return reverse('posts:detail', kwargs={'pk':self.object.pk})


@method_decorator(HAS_OWNERSHIP, 'get')
@method_decorator(HAS_OWNERSHIP, 'post')
class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('posts:list')

    # 서버에 저장된 원본 이미지 삭제
    def post(self, request, *args, **kwargs):
        post = Post.objects.get(pk=request.POST.get('post_id'))
        if post.postimage_set.exists():  # PostImage에 하나라도 이미지를 갖는다면
            for image_object in post.postimage_set.all():
                image_object.image.delete()

        return super().post(request, *args, **kwargs)


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class PostLikeView(UpdateView):
    def post(self, request, *args, **kwargs):
        user = User.objects.get(pk=request.user.pk)
        target_post = Post.objects.get(pk=request.POST.get('post_id'))

        if user in target_post.like_users.all():
            target_post.like_users.remove(user)
            target_post.likes -= 1
            target_post.save()
        else:
            target_post.like_users.add(user)
            target_post.likes += 1
            target_post.save()

        return HttpResponse(json.dumps(target_post.likes), content_type='application/json')