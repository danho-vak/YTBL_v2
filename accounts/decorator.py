from django.shortcuts import get_object_or_404, redirect

from accounts.models import User


def account_ownership_required(func):
    def decorated(request, *args, **kwargs):
        user = get_object_or_404(User, pk=kwargs['pk'])
        if not user == request.user:
            return redirect('accounts:login')
        return func(request, *args, **kwargs)
    return decorated