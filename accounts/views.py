from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, FormView, DeleteView

from accounts.decorator import account_ownership_required
from accounts.forms import CustomUserCreationForm
from accounts.models import User


# define custom decorator
has_ownership = [account_ownership_required, login_required]


class AccountCreateView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'accounts/create.html'
    success_url = reverse_lazy('maps:map')


# logout는 내장 제네릭뷰를 통해 urls.py에 구현
class AccountLoginView(LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('maps:map')


@method_decorator(has_ownership, 'get')
class AccountDetailView(DetailView):
    model = User
    template_name = 'accounts/detail.html'
    context_object_name = 'target_user'


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountPWChangeView(FormView):
    model = User
    form_class = PasswordChangeForm
    template_name = 'accounts/update.html'
    
    def get_form_kwargs(self):  # PasswordChangeForm의 파라미터를 건내줄 함수
        kwargs = super(AccountPWChangeView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        if self.request.method == 'POST':
            kwargs['data'] = self.request.POST
        return kwargs
    
    def form_valid(self, form):  # Validation check후 save 및 session에 변경된 비밀번호를 건내주고 session 유지
        form.save()
        update_session_auth_hash(self.request, form.user)
        return super(AccountPWChangeView, self).form_valid(form)
    
    def get_success_url(self):  # 변경 후 다시 detail로
        return reverse('accounts:detail', kwargs={'pk':self.request.user.pk})


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    template_name = 'accounts/delete.html'
    success_url = reverse_lazy('maps:map')