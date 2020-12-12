from django.urls import path

from accounts.views import AccountCreateView

app_name = 'accounts'

urlpatterns = [
    path('create/', AccountCreateView.as_view(), name='create'),
]