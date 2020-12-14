from django import forms

from posts.models import PostImage, Post


class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']
        exclude = ['likes', 'like_users']


class PostImageCreationForm(forms.ModelForm):
    class Meta:
        model = PostImage
        fields = ['image']