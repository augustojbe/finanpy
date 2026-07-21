from datetime import date

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.views.generic import TemplateView

from accounts.models import Account
from transactions.models import Transaction


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        now = date.today()
        transactions = Transaction.objects.filter(user=self.request.user)
        current_month_transactions = transactions.filter(
            date__month=now.month, date__year=now.year
        )

        total_income = current_month_transactions.filter(
            transaction_type='income'
        ).aggregate(total=Sum('amount'))['total'] or 0
        total_expense = current_month_transactions.filter(
            transaction_type='expense'
        ).aggregate(total=Sum('amount'))['total'] or 0
        balance = total_income - total_expense

        recent_transactions = transactions.select_related(
            'account', 'category'
        )[:5]

        accounts = Account.objects.filter(
            user=self.request.user, is_active=True
        )
        accounts_with_balances = []
        for account in accounts:
            accounts_with_balances.append({
                'account': account,
                'balance': account.get_current_balance(),
            })

        month_names = {
            1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril',
            5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'Agosto',
            9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro',
        }
        current_period = f'{month_names[now.month]} {now.year}'

        context.update({
            'total_income': total_income,
            'total_expense': total_expense,
            'balance': balance,
            'recent_transactions': recent_transactions,
            'accounts': accounts_with_balances,
            'current_period': current_period,
        })
        return context
