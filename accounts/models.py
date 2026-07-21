from django.conf import settings
from django.db import models


class Account(models.Model):

    class AccountType(models.TextChoices):
        CHECKING = 'checking', 'Conta Corrente'
        SAVINGS = 'savings', 'Poupança'
        WALLET = 'wallet', 'Carteira'
        INVESTMENT = 'investment', 'Investimento'

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='accounts',
    )
    name = models.CharField(max_length=150)
    account_type = models.CharField(
        max_length=20,
        choices=AccountType.choices,
        default=AccountType.CHECKING,
    )
    initial_balance = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_current_balance(self):
        from django.db.models import Sum

        try:
            from transactions.models import Transaction
        except ImportError:
            return self.initial_balance

        incomes = Transaction.objects.filter(
            account=self, transaction_type='income'
        ).aggregate(total=Sum('amount'))['total'] or 0
        expenses = Transaction.objects.filter(
            account=self, transaction_type='expense'
        ).aggregate(total=Sum('amount'))['total'] or 0
        return self.initial_balance + incomes - expenses
