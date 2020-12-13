
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm

from accounts.models import User


# UserCreationForm을 상속받는 Custom User Model용 Creation Form
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):  # Meta 클래스에 Custom User Model을 명시해준다
        model = User
        fields = ['email', 'username']
        labels = {
            'email': '이메일',
            'username': '닉네임'
        }
