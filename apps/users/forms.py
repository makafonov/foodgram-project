from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    UsernameField,
)


User = get_user_model()


class UserRegistrationForm(UserCreationForm):
    password2 = None

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'username', 'email')


class UserLoginForm(AuthenticationForm):
    username = UsernameField(
        label='Имя',
        widget=forms.TextInput(attrs={'autofocus': True}),
    )

    error_messages = {
        'invalid_login':
            ' '.join(
                [
                    'Имя пользователя и пароль не совпадают.',
                    'Введите правильные данные.',
                ],
            ),
    }
