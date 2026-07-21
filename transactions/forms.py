from django import forms
from django.core.exceptions import ValidationError
from django.db.models import Q

from accounts.models import Account
from categories.models import Category

from .models import Transaction


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('transaction_type', 'description', 'amount', 'date',
                  'account', 'category', 'notes')
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        base_classes = (
            'w-full bg-gray-800 border border-gray-700 text-white '
            'rounded-lg px-4 py-2.5 '
            'focus:outline-none focus:ring-2 focus:ring-violet-500 '
            'focus:border-transparent transition-all duration-200'
        )

        textarea_classes = base_classes + ' resize-none'

        for field_name in self.fields:
            widget = self.fields[field_name].widget
            css = textarea_classes if isinstance(widget, forms.Textarea) else base_classes
            widget.attrs.update({'class': css})

        if self.user:
            self.fields['account'].queryset = Account.objects.filter(
                user=self.user
            )
            self.fields['category'].queryset = Category.objects.filter(
                Q(user=self.user) | Q(user__isnull=True)
            )

        self.fields['transaction_type'].label = 'Tipo'
        self.fields['description'].label = 'Descrição'
        self.fields['amount'].label = 'Valor'
        self.fields['date'].label = 'Data'
        self.fields['account'].label = 'Conta'
        self.fields['category'].label = 'Categoria'
        self.fields['notes'].label = 'Observações'

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount is not None and amount <= 0:
            raise ValidationError('O valor deve ser maior que zero.')
        return amount
