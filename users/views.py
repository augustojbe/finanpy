from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView as AuthLoginView, LogoutView as AuthLogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from users.forms import UserLoginForm, UserRegistrationForm


class LandingPageView(TemplateView):
    template_name = 'landing.html'


class RegisterView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        response = super().form_valid(form)
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password1')
        user = authenticate(self.request, email=email, password=password)
        if user:
            login(self.request, user)
        messages.success(self.request, 'Conta criada com sucesso. Bem-vindo ao Finanpy!')
        return response


class LoginView(AuthLoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'
    redirect_authenticated_user = True


class LogoutView(AuthLogoutView):
    http_method_names = ['post', 'get', 'options']

