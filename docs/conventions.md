# Convenções — Padrões de Código

## Linguagem

| Contexto | Idioma |
|---|---|
| Código-fonte (variáveis, funções, classes, comentários) | **Inglês** |
| Interface do usuário (templates, labels, mensagens) | **Português Brasileiro** |

---

## Estilo de código Python

O projeto segue a [PEP 8](https://peps.python.org/pep-0008/).

### Aspas

Use **sempre aspas simples** em strings Python.

```python
# ✅ correto
name = 'Finanpy'
verbose_name = 'conta bancária'

# ❌ evitar
name = "Finanpy"
```

A única exceção é quando a string contém aspas simples internamente:

```python
message = "it's a valid exception"
```

---

### Nomes

| Tipo | Convenção | Exemplo |
|---|---|---|
| Variáveis e funções | `snake_case` | `total_income`, `get_balance()` |
| Classes | `PascalCase` | `CustomUser`, `TransactionListView` |
| Constantes | `UPPER_SNAKE_CASE` | `MAX_AMOUNT` |
| Apps Django | `snake_case` (singular) | `accounts`, `users` |
| Models | `PascalCase` (singular) | `Account`, `Transaction` |

---

### Importações

Ordem obrigatória (PEP 8):

```python
# 1. Biblioteca padrão Python
import os
from datetime import date

# 2. Dependências de terceiros
from django.db import models
from django.contrib.auth import get_user_model

# 3. Imports do próprio projeto
from accounts.models import Account
```

---

## Views

**Preferir Class-Based Views (CBV)** sempre que possível.

```python
# ✅ preferido
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

class AccountListView(LoginRequiredMixin, ListView):
    model = Account
    template_name = 'accounts/account_list.html'
    context_object_name = 'accounts'

    def get_queryset(self):
        return Account.objects.filter(user=self.request.user)
```

Usar Function-Based Views (FBV) apenas em casos onde a CBV tornaria o código
mais complexo que o necessário.

---

## Models

Todo model deve:

1. Ter os campos `created_at` e `updated_at`.
2. Definir `__str__()`.
3. Ter `class Meta` com ao menos `ordering` quando relevante.
4. Filtrar dados sempre por usuário para garantir isolamento.

```python
class Account(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
```

---

## Segurança de dados

Toda query que retorna dados de usuário **deve filtrar por `user=request.user`**.
Nunca retornar dados de todos os usuários em views autenticadas.

```python
# ✅ correto — filtra pelo usuário da sessão
def get_queryset(self):
    return Transaction.objects.filter(user=self.request.user)

# ❌ nunca fazer isto em views autenticadas
def get_queryset(self):
    return Transaction.objects.all()
```

---

## Formulários

- Usar `ModelForm` sempre que o form mapeia diretamente um model.
- Validações de campo ficam em métodos `clean_<campo>()` dentro do form.
- Nunca colocar lógica de negócio em templates.

```python
class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['name', 'account_type', 'initial_balance']

    def clean_initial_balance(self):
        value = self.cleaned_data['initial_balance']
        if value < 0:
            raise forms.ValidationError('O saldo inicial não pode ser negativo.')
        return value
```

---

## Signals

Quando o projeto usar signals:

- O signal fica em um arquivo `signals.py` dentro da app correspondente.
- O signal é registrado no método `ready()` do `AppConfig` da app.

```python
# profiles/apps.py
class ProfilesConfig(AppConfig):
    name = 'profiles'

    def ready(self):
        import profiles.signals  # noqa: F401
```

---

## Templates

- Templates globais ficam em `templates/` na raiz do projeto.
- Templates de cada app ficam em `<app>/templates/<app>/`.
- Todo template de página autenticada herda do template base com sidebar.
- Todo template de página pública herda do template base simples.
- Toda string visível ao usuário deve estar em **português brasileiro**.

### Estrutura de nomes de template

```
templates/
├── base.html              # base para páginas públicas
├── base_auth.html         # base para páginas autenticadas (com sidebar)
├── dashboard.html         # dashboard principal
└── landing.html           # página pública de apresentação

accounts/templates/accounts/
├── account_list.html
├── account_form.html
└── account_confirm_delete.html
```

---

## URLs

- Cada app define seu próprio `urls.py`.
- `core/urls.py` inclui as URLs de cada app via `include()`.
- Usar `name=` em todos os `path()` para permitir `{% url %}` nos templates.

```python
# accounts/urls.py
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.AccountListView.as_view(), name='list'),
    path('novo/', views.AccountCreateView.as_view(), name='create'),
    path('<int:pk>/editar/', views.AccountUpdateView.as_view(), name='update'),
    path('<int:pk>/excluir/', views.AccountDeleteView.as_view(), name='delete'),
]
```

---

## Mensagens ao usuário

Usar o sistema nativo de mensagens do Django (`django.contrib.messages`) para
feedback de ações. As mensagens são renderizadas no template base.

```python
from django.contrib import messages

# em uma view
messages.success(request, 'Conta criada com sucesso.')
messages.error(request, 'Não foi possível excluir a conta.')
```
