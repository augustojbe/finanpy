from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import CategoryForm
from .models import Category


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'categories/category_list.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return Category.objects.filter(
            Q(user=self.request.user) | Q(user__isnull=True)
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_categories'] = Category.objects.filter(
            user=self.request.user
        )
        context['default_categories'] = Category.objects.filter(
            user__isnull=True
        )
        return context


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'categories/category_form.html'
    success_url = reverse_lazy('categories:list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Categoria criada com sucesso.')
        return super().form_valid(form)


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'categories/category_form.html'
    success_url = reverse_lazy('categories:list')

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, 'Categoria atualizada com sucesso.')
        return super().form_valid(form)


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'categories/category_confirm_delete.html'
    success_url = reverse_lazy('categories:list')

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)

    def form_valid(self, form):
        category = self.get_object()
        if category.is_default:
            messages.error(
                self.request,
                'Não é possível excluir uma categoria padrão do sistema.',
            )
            return super().form_invalid(form)
        try:
            if category.transaction_set.exists():
                messages.error(
                    self.request,
                    'Não foi possível excluir a categoria pois existem transações vinculadas a ela.',
                )
                return super().form_invalid(form)
        except AttributeError:
            pass
        messages.success(self.request, 'Categoria excluída com sucesso.')
        return super().form_valid(form)
