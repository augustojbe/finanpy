from django.contrib import admin
from django.contrib.admin import register

from profiles.models import Profile


@register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'created_at')
    search_fields = ('user__email', 'user__first_name', 'user__last_name')
