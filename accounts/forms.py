from django import forms

from .models import Account


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('name', 'account_type', 'initial_balance')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({
                'class': 'w-full bg-gray-800 border border-gray-700 text-white rounded-lg px-4 py-2.5 focus:outline-none focus:ring-2 focus:ring-violet-500 focus:border-transparent transition-all duration-200',
            })
        self.fields['name'].label = 'Nome'
        self.fields['account_type'].label = 'Tipo de conta'
        self.fields['initial_balance'].label = 'Saldo inicial'
