from django.http import HttpResponseForbidden

from comments.models import Comment


def comment_ownership_required(func):
    def decorated(request, *args, **kwargs):
        comment = Comment.objects.get(pk=kwargs['comment_id'])
        if not comment.author == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated