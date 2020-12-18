from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView, ListView

from comments.decorator import comment_ownership_required
from comments.forms import CommentCreationForm
from comments.models import Comment
from posts.models import Post


HAS_OWNERSHIP = [comment_ownership_required, login_required]


'''
    Parent Comment Creation View
'''
@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreationForm

    def form_valid(self, form):
        new_form = form.save(commit=False)
        new_form.author = self.request.user
        new_form.post = Post.objects.get(pk=self.request.POST.get('post_id'))
        new_form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('posts:detail', kwargs={'pk': self.request.POST.get('post_id')})


'''
    Child Comment Creation View
'''
@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class CommentChildCreateView(CreateView):
    model = Comment
    form_class = CommentCreationForm

    def form_valid(self, form):
        new_form = form.save(commit=False)
        new_form.author = self.request.user
        new_form.post = Post.objects.get(pk=self.request.POST.get('post_id'))
        new_form.parent = Comment.objects.get(pk=self.request.POST.get('parent_id'))
        new_form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('posts:detail', kwargs={'pk': self.request.POST.get('post_id')})


'''
    Comment Deletion View
'''
@method_decorator(HAS_OWNERSHIP, 'get')
@method_decorator(HAS_OWNERSHIP, 'post')
class CommentDeleteView(DeleteView):
    model = Comment

    def get_object(self, queryset=None):
        object = Comment.objects.get(pk=self.request.POST.get('comment_id'))
        return object

    def get_success_url(self):
        return reverse('posts:detail', kwargs={'pk': self.object.post.pk})


'''
   Last Comment object View
'''
class GetLastCommentView(ListView):
    template_name = 'comments/snippets/last_comment.html'
    context_object_name = 'comment'

    def get_queryset(self):
        last_comment = Comment.objects.filter(post=self.request.GET.get('post_id')).last()
        return last_comment


