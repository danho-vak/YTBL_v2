from django.urls import path

from comments.views import CommentCreateView, CommentDeleteView, GetLastCommentView

app_name = 'comments'

urlpatterns = [
    path('create/<int:post_id>', CommentCreateView.as_view(), name='create'),
    path('delete/<int:comment_id>', CommentDeleteView.as_view(), name='delete'),
    path('last/<int:post_id>', GetLastCommentView.as_view(), name='last'),
]