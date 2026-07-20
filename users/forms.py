from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import ValidationError

User = get_user_model()


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30,
        required=True,
        label='Nome',
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
        label='Sobrenome',
    )
    email = forms.EmailField(
        max_length=254,
        required=True,
        label='E-mail',
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).exists():
            raise ValidationError('Este e-mail já está cadastrado.')
        return email


class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(
        max_length=254,
        required=True,
        label='E-mail',
        widget=forms.EmailInput(attrs={'autofocus': True}),
    )
    password = forms.CharField(
        label='Senha',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
    )
