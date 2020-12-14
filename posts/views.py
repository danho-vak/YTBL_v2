from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView
from django.views.generic.edit import FormMixin
from django.views.generic.list import MultipleObjectMixin

from accounts.models import User
from posts.decorator import account_ownership_required
from posts.forms import PostCreationForm
from posts.models import Post, PostImage

has_ownership = [account_ownership_required, login_required]


class PostListView(ListView, FormMixin, MultipleObjectMixin):
    model = Post
    context_object_name = 'post_list'
    form_class = PostCreationForm
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
        return reverse_lazy('posts:list')
