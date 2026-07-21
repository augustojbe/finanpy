from django.contrib import admin
from django.urls import include, path

from core.views import DashboardView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('contas/', include('accounts.urls')),
    path('categorias/', include('categories.urls')),
    path('transacoes/', include('transactions.urls')),
    path('perfil/', include('profiles.urls')),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]

handler404 = 'django.views.defaults.page_not_found'
handler500 = 'django.views.defaults.server_error'
