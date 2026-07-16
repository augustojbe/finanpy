# CLAUDE.md — Finanpy

Guia de contexto para o assistente de IA. Leia este arquivo antes de qualquer
interação com o projeto.

---

## O que é este projeto

**Finanpy** é um sistema web de gestão de finanças pessoais.
Stack: Python + Django 6 (full stack), Django Template Language, TailwindCSS,
SQLite.

Filosofia: **simples e enxuto**. Sem over-engineering. Sem dependências
desnecessárias. Usar ao máximo os recursos nativos do Django.

Documentação completa:
- `prd.md` — Product Requirements Document
- `docs/setup.md` — como rodar o projeto
- `docs/architecture.md` — estrutura de apps e roteamento
- `docs/conventions.md` — padrões de código
- `docs/design-system.md` — paleta, componentes e TailwindCSS

---

## Stack

| Camada | Tecnologia |
|---|---|
| Linguagem | Python 3.12+ |
| Framework | Django 6.0.7 |
| Templates | Django Template Language (DTL) |
| CSS | TailwindCSS via CDN |
| Banco de dados | SQLite (padrão Django) |
| Autenticação | Django Auth nativo, login por e-mail |
| Views | Class-Based Views (preferencial) |

---

## Estrutura de apps

```
finanpy/
├── accounts/      # contas bancárias do usuário
├── categories/    # categorias de transações
├── core/          # settings, urls raiz, wsgi, asgi
├── profiles/      # perfil do usuário (1:1 com CustomUser)
├── transactions/  # transações financeiras (receitas e despesas)
├── users/         # CustomUser, login por e-mail, registro, logout
├── docs/          # documentação do projeto
├── prd.md
├── manage.py
└── requirements.txt
```

Dentro de cada app, a estrutura esperada é:

```
<app>/
├── migrations/
├── __init__.py
├── admin.py
├── apps.py
├── forms.py        # criado quando necessário
├── models.py
├── signals.py      # criado quando a app usa signals
├── urls.py         # criado quando necessário
├── views.py
└── templates/
    └── <app>/
        └── *.html
```

Templates globais ficam em `templates/` na raiz do projeto.

---

## Regras de código — siga sempre

### Idioma

- **Código-fonte** (variáveis, funções, classes, comentários): **inglês**
- **Interface do usuário** (templates, labels, mensagens, textos): **português brasileiro**

### Python

- Seguir **PEP 8** rigorosamente.
- Usar **aspas simples** em todas as strings. Aspas duplas apenas quando a
  string contém aspas simples internamente.
- Nomes: `snake_case` para variáveis/funções, `PascalCase` para classes,
  `UPPER_SNAKE_CASE` para constantes.
- Ordem de imports: stdlib → terceiros (Django) → projeto.

```python
# ✅ correto
name = 'Finanpy'
verbose_name = 'conta bancária'

# ❌ evitar
name = "Finanpy"
```

### Views

- **Preferir Class-Based Views (CBV)** sempre.
- Toda view autenticada usa `LoginRequiredMixin` como primeiro mixin.
- FBV apenas quando CBV tornaria o código desnecessariamente complexo.

```python
class AccountListView(LoginRequiredMixin, ListView):
    model = Account
    template_name = 'accounts/account_list.html'
    context_object_name = 'accounts'

    def get_queryset(self):
        return Account.objects.filter(user=self.request.user)
```

### Models

Todo model **obrigatoriamente** deve ter:

1. `created_at = models.DateTimeField(auto_now_add=True)`
2. `updated_at = models.DateTimeField(auto_now=True)`
3. `__str__()` definido
4. `class Meta` com `ordering` quando relevante

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

### Segurança de dados

**Toda query em view autenticada filtra por `user=self.request.user`.**
Nunca usar `.all()` em dados de usuário sem filtro.

```python
# ✅ sempre assim
def get_queryset(self):
    return Transaction.objects.filter(user=self.request.user)

# ❌ jamais em views autenticadas
def get_queryset(self):
    return Transaction.objects.all()
```

### Formulários

- Usar `ModelForm` quando o form mapeia um model.
- Validações de campo em `clean_<campo>()` dentro do form.
- Nunca colocar lógica de negócio em templates.

### Signals

- O signal fica em `<app>/signals.py`.
- Registrado no `ready()` do `AppConfig` em `<app>/apps.py`.

```python
# profiles/apps.py
class ProfilesConfig(AppConfig):
    name = 'profiles'

    def ready(self):
        import profiles.signals  # noqa: F401
```

### URLs

- Cada app tem seu próprio `urls.py` com `app_name` definido.
- Todos os `path()` têm `name=` para uso em `{% url %}`.
- `core/urls.py` inclui as URLs de cada app via `include()`.

### Templates

- Herança obrigatória: todo template herda de `base.html` ou `base_auth.html`.
- Páginas autenticadas herdam de `base_auth.html` (layout com sidebar).
- Páginas públicas herdam de `base.html`.
- Toda string visível ao usuário em **português brasileiro**.

### Mensagens ao usuário

Usar o sistema nativo `django.contrib.messages`.

```python
messages.success(request, 'Conta criada com sucesso.')
messages.error(request, 'Não foi possível excluir a conta.')
```

---

## Autenticação

- Model: `users.CustomUser` (herda de `AbstractUser`).
- `AUTH_USER_MODEL = 'users.CustomUser'` no `settings.py`.
- Login via **e-mail** (não username) — backend em `users/backends.py`.
- `USERNAME_FIELD = 'email'` no `CustomUser`.

> ⚠️ `AUTH_USER_MODEL` deve ser definido **antes da primeira migration**.

---

## Design system (TailwindCSS)

Design dark mode. Paleta principal:

| Papel | Classe |
|---|---|
| Fundo global | `bg-gray-950` |
| Card / painel | `bg-gray-900 border border-gray-800 rounded-xl` |
| Input | `bg-gray-800 border border-gray-700 rounded-lg` |
| Botão primário | `bg-gradient-to-r from-violet-600 to-indigo-600` |
| Receita | `text-emerald-400` |
| Despesa | `text-rose-400` |
| Label | `text-gray-400` |
| Texto principal | `text-white` |

Fonte: **Inter** (Google Fonts), aplicada no `<body>` com `font-['Inter']`.

Logo:
```html
<span class="bg-gradient-to-r from-violet-400 to-indigo-400 bg-clip-text text-transparent font-bold">
    Finanpy
</span>
```

Consulte `docs/design-system.md` para todos os componentes (botões, inputs,
cards, tabelas, badges, sidebar, alertas).

---

## O que NÃO fazer

- Não adicionar dependências além das já existentes sem solicitação explícita.
- Não implementar Docker (previsto para sprints finais).
- Não implementar testes automatizados (previsto para sprints finais).
- Não criar endpoints de API REST.
- Não usar aspas duplas em strings Python.
- Não usar FBV quando CBV resolve de forma simples.
- Não colocar lógica de negócio em templates.
- Não retornar dados de um usuário para outro.
- Não criar model sem `created_at` e `updated_at`.
- Não criar funcionalidade que não esteja descrita no `prd.md`.

---

## Comandos úteis

```bash
# Ativar virtualenv
source .venv/bin/activate

# Instalar dependências
pip install -r requirements.txt

# Criar migrations
python manage.py makemigrations

# Aplicar migrations
python manage.py migrate

# Rodar servidor de desenvolvimento
python manage.py runserver

# Criar superusuário
python manage.py createsuperuser
```
