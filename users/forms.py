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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields[field_name]
            css_class = 'w-full bg-gray-800 border border-gray-700 text-white rounded-lg px-4 py-2.5 focus:outline-none focus:ring-2 focus:ring-violet-500 focus:border-transparent transition-all duration-200'
            if field_name in ('password1', 'password2'):
                field.widget.attrs.update({
                    'class': css_class,
                    'placeholder': 'Mínimo de 8 caracteres' if field_name == 'password1' else 'Repita a senha',
                })
            else:
                field.widget.attrs.update({'class': css_class})

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
