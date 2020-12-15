from django.http import HttpResponseForbidden

from posts.models import Post


def post_ownership_required(func):
    def decorated(request, *args, **kwargs):
        post = Post.objects.get(pk=kwargs['pk'])
        if not post.author == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated