from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView

from comments.forms import CommentCreationForm
from comments.models import Comment
from posts.models import Post


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