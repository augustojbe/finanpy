from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from profiles.forms import PasswordChangeForm, ProfileForm, UserUpdateForm
from profiles.models import Profile


class ProfileView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'profiles/profile.html'
    success_url = reverse_lazy('profiles:profile')

    def get_object(self, queryset=None):
        return self.request.user.profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'user_form' not in kwargs:
            context['user_form'] = UserUpdateForm(instance=self.request.user)
        if 'password_form' not in kwargs:
            context['password_form'] = PasswordChangeForm(user=self.request.user)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        action = request.POST.get('action', '')

        if action == 'change_password':
            return self._handle_password_change(request)
        else:
            return self._handle_profile_update(request)

    def _handle_profile_update(self, request):
        form = ProfileForm(request.POST, instance=self.object)
        user_form = UserUpdateForm(request.POST, instance=request.user)

        if form.is_valid() and user_form.is_valid():
            form.save()
            user_form.save()
            messages.success(request, 'Perfil atualizado com sucesso.')
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def _handle_password_change(self, request):
        form = PasswordChangeForm(user=request.user, data=request.POST)

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Senha alterada com sucesso.')
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
