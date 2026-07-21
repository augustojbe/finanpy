import calendar
from datetime import date

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q, Sum
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from categories.models import Category

from .forms import TransactionForm
from .models import Transaction


class TransactionListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'transactions/transaction_list.html'
    context_object_name = 'transactions'
    paginate_by = 20

    def get_queryset(self):
        qs = Transaction.objects.filter(
            user=self.request.user
        ).select_related('account', 'category')

        month = self._get_month()
        year = self._get_year()
        ttype = self.request.GET.get('type', '')
        category_pk = self.request.GET.get('category', '')

        if month and year:
            last_day = calendar.monthrange(year, month)[1]
            qs = qs.filter(
                date__gte=date(year, month, 1),
                date__lte=date(year, month, last_day),
            )

        if ttype in ('income', 'expense'):
            qs = qs.filter(transaction_type=ttype)

        if category_pk:
            qs = qs.filter(category_id=category_pk)

        return qs

    def _get_month(self):
        month = self.request.GET.get('month', '')
        if month and month.isdigit():
            m = int(month)
            if 1 <= m <= 12:
                return m
        return date.today().month

    def _get_year(self):
        year = self.request.GET.get('year', '')
        if year and year.isdigit() and len(year) == 4:
            return int(year)
        return date.today().year

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        qs = Transaction.objects.filter(user=self.request.user)

        month = self._get_month()
        year = self._get_year()
        last_day = calendar.monthrange(year, month)[1]

        month_qs = qs.filter(
            date__gte=date(year, month, 1),
            date__lte=date(year, month, last_day),
        )

        total_income = month_qs.filter(
            transaction_type='income'
        ).aggregate(total=Sum('amount'))['total'] or 0
        total_expense = month_qs.filter(
            transaction_type='expense'
        ).aggregate(total=Sum('amount'))['total'] or 0

        context['total_income'] = total_income
        context['total_expense'] = total_expense
        context['balance'] = total_income - total_expense
        context['categories'] = Category.objects.filter(
            Q(user=self.request.user) | Q(user__isnull=True)
        )
        context['selected_month'] = month
        context['selected_year'] = year
        context['selected_type'] = self.request.GET.get('type', '')
        context['selected_category'] = self.request.GET.get('category', '')
        context['month_options'] = list(range(1, 13))
        context['year_options'] = list(range(year - 5, year + 2))

        return context


class TransactionCreateView(LoginRequiredMixin, CreateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'transactions/transaction_form.html'
    success_url = reverse_lazy('transactions:list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Transação registrada com sucesso.')
        return super().form_valid(form)


class TransactionUpdateView(LoginRequiredMixin, UpdateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'transactions/transaction_form.html'
    success_url = reverse_lazy('transactions:list')

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        messages.success(self.request, 'Transação atualizada com sucesso.')
        return super().form_valid(form)


class TransactionDeleteView(LoginRequiredMixin, DeleteView):
    model = Transaction
    template_name = 'transactions/transaction_confirm_delete.html'
    success_url = reverse_lazy('transactions:list')

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, 'Transação excluída com sucesso.')
        return super().form_valid(form)
