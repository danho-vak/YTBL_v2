from django.contrib.auth.views import LogoutView
from django.urls import path

from accounts.views import AccountCreateView, AccountLoginView, AccountDetailView, AccountPWChangeView, \
    AccountDeleteView

app_name = 'accounts'

urlpatterns = [
    path('create/', AccountCreateView.as_view(), name='create'),
    path('login/', AccountLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),
    path('update/<int:pk>', AccountPWChangeView.as_view(), name='update'),
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),  # DeleteView는 CBV가 아님 FBV
]