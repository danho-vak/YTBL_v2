from django.urls import path

from posts.views import PostListView, PostCreateView, PostDetailView, PostUpdateView, PostDeleteView, PostLikeView

app_name = 'posts'

urlpatterns = [
    path('', PostListView.as_view(), name='list'),
    path('create/', PostCreateView.as_view(), name='create'),
    path('detail/<int:pk>', PostDetailView.as_view(), name='detail'),
    path('update/<int:pk>', PostUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='delete'),
    path('like/<int:pk>', PostLikeView.as_view(), name='like'),
]