from django.conf import settings
from django.db import models


class CategoryType(models.TextChoices):
    INCOME = 'income', 'Receita'
    EXPENSE = 'expense', 'Despesa'


class Category(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='categories',
    )
    name = models.CharField(max_length=100)
    category_type = models.CharField(
        max_length=10,
        choices=CategoryType.choices,
    )
    icon = models.CharField(max_length=10, blank=True)
    is_default = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        unique_together = ['user', 'name', 'category_type']

    def __str__(self):
        return f'{self.icon} {self.name}' if self.icon else self.name
