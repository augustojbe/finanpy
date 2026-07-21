from django.conf import settings
from django.db import models


class TransactionType(models.TextChoices):
    INCOME = 'income', 'Receita'
    EXPENSE = 'expense', 'Despesa'


class Transaction(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='transactions',
    )
    account = models.ForeignKey(
        'accounts.Account',
        on_delete=models.PROTECT,
    )
    category = models.ForeignKey(
        'categories.Category',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    transaction_type = models.CharField(
        max_length=10,
        choices=TransactionType.choices,
    )
    amount = models.DecimalField(max_digits=14, decimal_places=2)
    description = models.CharField(max_length=300)
    date = models.DateField()
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date', '-created_at']
        indexes = [
            models.Index(fields=['user']),
            models.Index(fields=['date']),
            models.Index(fields=['transaction_type']),
        ]

    def __str__(self):
        return f'{self.description} — {self.amount}'
