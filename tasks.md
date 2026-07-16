## Lista de Tarefas (Sprints)

---

### 🏁 Sprint 0 — Setup e Fundação do Projeto ✅

**Objetivo:** Preparar o ambiente, configurações globais e estrutura base do projeto.

---

- [x ] **0.1 — Configuração do Ambiente Python**
  - [x] 0.1.1 — Criar e ativar virtualenv (`python -m venv .venv`)
  - [ x] 0.1.2 — Instalar Django 6.x (`pip install django`)
  - [x ] 0.1.3 — Gerar `requirements.txt` (`pip freeze > requirements.txt`)
  - [x ] 0.1.4 — Criar arquivo `.gitignore` com: `.venv/`, `db.sqlite3`, `*.pyc`, `__pycache__/`, `.env`
  - [x ] 0.1.5 — Criar arquivo `.env` para variáveis sensíveis e adicionar ao `.gitignore`

- [x] **0.2 — Configuração do `settings.py`**
  - [x] 0.2.1 — Mover `SECRET_KEY` para variável de ambiente (usando `os.environ.get` ou `python-decouple`)
  - [x] 0.2.2 — Configurar `AUTH_USER_MODEL = 'users.CustomUser'` (antes de qualquer migration)
  - [x] 0.2.3 — Adicionar todos os apps ao `INSTALLED_APPS`: `accounts`, `categories`, `profiles`, `transactions`, `users`
  - [x] 0.2.4 — Configurar `LANGUAGE_CODE = 'pt-br'` e `TIME_ZONE = 'America/Sao_Paulo'`
  - [x] 0.2.5 — Configurar diretório de templates globais: `TEMPLATES[0]['DIRS'] = [BASE_DIR / 'templates']`
  - [x] 0.2.6 — Configurar `STATIC_URL` e `STATICFILES_DIRS`
  - [x] 0.2.7 — Configurar `LOGIN_URL`, `LOGIN_REDIRECT_URL` e `LOGOUT_REDIRECT_URL`

- [x] **0.3 — Configuração de URLs raiz (`core/urls.py`)**
  - [x] 0.3.1 — Incluir `path('', include('users.urls'))` para landing e autenticação
  - [x] 0.3.2 — Incluir `path('contas/', include('accounts.urls'))`
  - [x] 0.3.3 — Incluir `path('categorias/', include('categories.urls'))`
  - [x] 0.3.4 — Incluir `path('transacoes/', include('transactions.urls'))`
  - [x] 0.3.5 — Incluir `path('perfil/', include('profiles.urls'))`
  - [x] 0.3.6 — Incluir `path('dashboard/', include('core_views'))` ou criar view de dashboard em app dedicada

- [x] **0.4 — Template Base Global (`templates/base.html`)**
  - [x] 0.4.1 — Criar arquivo `templates/base.html` com estrutura HTML5 completa
  - [x] 0.4.2 — Incluir link da fonte Inter do Google Fonts
  - [x] 0.4.3 — Incluir CDN do TailwindCSS Play (`<script src="https://cdn.tailwindcss.com"></script>`)
  - [x] 0.4.4 — Definir bloco `{% block title %}` para título dinâmico por página
  - [x] 0.4.5 — Definir bloco `{% block content %}` para conteúdo de cada página
  - [x] 0.4.6 — Implementar renderização de mensagens Django Messages com estilo do design system
  - [x] 0.4.7 — Criar `templates/base_auth.html` (layout com sidebar) herdando de `base.html`
  - [x] 0.4.8 — Implementar sidebar com: logo Finanpy, links de navegação, dados do usuário logado e botão de logout
  - [x] 0.4.9 — Implementar destaque de item ativo na sidebar usando `request.resolver_match.url_name`

---

### 🚀 Sprint 1 — App `users`: Autenticação e Usuário Customizado

**Objetivo:** Implementar modelo de usuário com login por e-mail e fluxos de autenticação.

---

- [x] **1.1 — Model `CustomUser` (`users/models.py`)**
  - [x] 1.1.1 — Criar classe `CustomUser` herdando de `AbstractUser`
  - [x] 1.1.2 — Adicionar campo `email = models.EmailField(unique=True)` (sem aspas duplas)
  - [x] 1.1.3 — Adicionar campos `created_at = models.DateTimeField(auto_now_add=True)` e `updated_at = models.DateTimeField(auto_now=True)`
  - [x] 1.1.4 — Definir `USERNAME_FIELD = 'email'`
  - [x] 1.1.5 — Definir `REQUIRED_FIELDS = ['first_name', 'last_name']` (remove username dos required)
  - [x] 1.1.6 — Adicionar campo `username` como opcional/nulo ou removê-lo (definir estratégia)
  - [x] 1.1.7 — Registrar no `admin.py` com `UserAdmin` customizado

- [x] **1.2 — Backend de Autenticação por E-mail (`users/backends.py`)**
  - [x] 1.2.1 — Criar classe `EmailBackend` herdando de `ModelBackend`
  - [x] 1.2.2 — Sobrescrever método `authenticate(request, email=None, password=None, **kwargs)`
  - [x] 1.2.3 — Buscar usuário por `email` ao invés de `username`
  - [x] 1.2.4 — Adicionar `AUTHENTICATION_BACKENDS = ['users.backends.EmailBackend']` no `settings.py`

- [ ] **1.3 — Formulários de Autenticação (`users/forms.py`)**
  - [ ] 1.3.1 — Criar `UserRegistrationForm` herdando de `UserCreationForm`
  - [ ] 1.3.2 — Adicionar campos: `first_name`, `last_name`, `email` no form de registro
  - [ ] 1.3.3 — Adicionar validação de e-mail único no método `clean_email()`
  - [ ] 1.3.4 — Criar `UserLoginForm` com campos `email` e `password`
  - [ ] 1.3.5 — Garantir que todos os campos usem aspas simples nas strings

- [ ] **1.4 — Views de Autenticação (`users/views.py`)**
  - [ ] 1.4.1 — Criar `LandingPageView` (TemplateView) para a página pública `/`
  - [ ] 1.4.2 — Criar `RegisterView` (FormView ou CreateView) para `/register/`
    - [ ] 1.4.2.1 — Usar `UserRegistrationForm`
    - [ ] 1.4.2.2 — Após sucesso: autenticar usuário automaticamente e redirecionar para dashboard
    - [ ] 1.4.2.3 — Adicionar mensagem de sucesso via `messages.success()`
  - [ ] 1.4.3 — Criar `LoginView` customizada (herdando de `auth.views.LoginView`)
    - [ ] 1.4.3.1 — Configurar `authentication_form` para usar `UserLoginForm`
    - [ ] 1.4.3.2 — Configurar `template_name = 'users/login.html'`
    - [ ] 1.4.3.3 — Configurar `redirect_authenticated_user = True`
  - [ ] 1.4.4 — Configurar `LogoutView` nativa do Django para `/logout/`

- [ ] **1.5 — URLs da App users (`users/urls.py`)**
  - [ ] 1.5.1 — Criar `urlpatterns` com: `path('', LandingPageView, name='landing')`
  - [ ] 1.5.2 — Adicionar `path('cadastro/', RegisterView, name='register')`
  - [ ] 1.5.3 — Adicionar `path('entrar/', LoginView, name='login')`
  - [ ] 1.5.4 — Adicionar `path('sair/', LogoutView, name='logout')`

- [ ] **1.6 — Templates de Autenticação**
  - [ ] 1.6.1 — Criar `templates/landing.html` (página pública de apresentação)
    - [ ] 1.6.1.1 — Header com logo e botões "Entrar" e "Cadastre-se"
    - [ ] 1.6.1.2 — Seção hero com gradiente e descrição do produto
    - [ ] 1.6.1.3 — Listar 3 features principais em cards
    - [ ] 1.6.1.4 — Footer simples com nome do produto
  - [ ] 1.6.2 — Criar `users/templates/users/register.html`
    - [ ] 1.6.2.1 — Layout centralizado com card de formulário (fundo escuro)
    - [ ] 1.6.2.2 — Logo Finanpy com gradiente no topo
    - [ ] 1.6.2.3 — Form com campos: primeiro nome, sobrenome, e-mail, senha, confirmar senha
    - [ ] 1.6.2.4 — Renderizar erros de formulário com estilo `text-rose-400`
    - [ ] 1.6.2.5 — Botão primário "Criar conta" com gradiente violet→indigo
    - [ ] 1.6.2.6 — Link para "Já tenho uma conta → Entrar"
  - [ ] 1.6.3 — Criar `users/templates/users/login.html`
    - [ ] 1.6.3.1 — Mesmo layout centralizado do registro
    - [ ] 1.6.3.2 — Form com campos: e-mail e senha
    - [ ] 1.6.3.3 — Renderizar mensagem de erro de credenciais inválidas
    - [ ] 1.6.3.4 — Botão primário "Entrar"
    - [ ] 1.6.3.5 — Link para "Não tenho conta → Cadastre-se"

- [ ] **1.7 — Migration e Teste Manual**
  - [ ] 1.7.1 — Rodar `python manage.py makemigrations users`
  - [ ] 1.7.2 — Rodar `python manage.py migrate`
  - [ ] 1.7.3 — Testar fluxo completo: acessar landing → cadastrar → logar → logout
  - [ ] 1.7.4 — Verificar que login com username falha e login com e-mail funciona

---

### 🧑‍💼 Sprint 2 — App `profiles`: Perfil do Usuário

**Objetivo:** Criar perfil automático de usuário via signal e tela de edição.

---

- [ ] **2.1 — Model `Profile` (`profiles/models.py`)**
  - [ ] 2.1.1 — Criar classe `Profile` com `OneToOneField` para `CustomUser`
  - [ ] 2.1.2 — Adicionar campo `phone = models.CharField(max_length=20, blank=True)`
  - [ ] 2.1.3 — Adicionar campos `created_at` e `updated_at`
  - [ ] 2.1.4 — Definir `__str__` retornando o email do usuário
  - [ ] 2.1.5 — Registrar no `admin.py`

- [ ] **2.2 — Signal de Criação Automática (`profiles/signals.py`)**
  - [ ] 2.2.1 — Criar arquivo `profiles/signals.py`
  - [ ] 2.2.2 — Importar `post_save` e `CustomUser`
  - [ ] 2.2.3 — Criar função `create_user_profile` decorada com `@receiver(post_save, sender=CustomUser)`
  - [ ] 2.2.4 — Usar `Profile.objects.get_or_create(user=instance)` dentro da função
  - [ ] 2.2.5 — Registrar o signal no método `ready()` do `ProfilesConfig` em `apps.py`
    - [ ] 2.2.5.1 — Sobrescrever `ready(self)` em `profiles/apps.py`
    - [ ] 2.2.5.2 — Adicionar `import profiles.signals` dentro do método `ready()`

- [ ] **2.3 — Formulários de Perfil (`profiles/forms.py`)**
  - [ ] 2.3.1 — Criar `ProfileForm` (ModelForm do Profile) com campo `phone`
  - [ ] 2.3.2 — Criar `UserUpdateForm` (ModelForm do CustomUser) com campos `first_name`, `last_name`
  - [ ] 2.3.3 — Criar `PasswordChangeForm` customizado ou usar nativo do Django

- [ ] **2.4 — Views de Perfil (`profiles/views.py`)**
  - [ ] 2.4.1 — Criar `ProfileView` (LoginRequiredMixin + UpdateView ou TemplateView)
  - [ ] 2.4.2 — Renderizar dois forms juntos: `UserUpdateForm` e `ProfileForm`
  - [ ] 2.4.3 — Salvar os dois forms no `post()` após validação
  - [ ] 2.4.4 — Adicionar `PasswordChangeView` usando view nativa do Django customizada com template do design system
  - [ ] 2.4.5 — Garantir que todas as views usam `LoginRequiredMixin`

- [ ] **2.5 — URLs e Templates de Perfil**
  - [ ] 2.5.1 — Criar `profiles/urls.py` com paths para perfil e alteração de senha
  - [ ] 2.5.2 — Criar `profiles/templates/profiles/profile.html`
    - [ ] 2.5.2.1 — Herdar de `base_auth.html` (layout com sidebar)
    - [ ] 2.5.2.2 — Seção de dados pessoais com form `UserUpdateForm` e `ProfileForm`
    - [ ] 2.5.2.3 — Seção separada para alteração de senha
    - [ ] 2.5.2.4 — Aplicar design system (inputs, botões, cards)

- [ ] **2.6 — Migration**
  - [ ] 2.6.1 — Rodar `python manage.py makemigrations profiles`
  - [ ] 2.6.2 — Rodar `python manage.py migrate`
  - [ ] 2.6.3 — Testar criação automática de perfil ao registrar novo usuário

---

### 🏦 Sprint 3 — App `accounts`: Contas Bancárias

**Objetivo:** CRUD completo de contas financeiras com cálculo de saldo.

---

- [ ] **3.1 — Model `Account` (`accounts/models.py`)**
  - [ ] 3.1.1 — Criar classe `Account` com os campos:
    - [ ] 3.1.1.1 — `user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)`
    - [ ] 3.1.1.2 — `name = CharField(max_length=150)`
    - [ ] 3.1.1.3 — `account_type = CharField(max_length=20, choices=AccountType.choices)`
    - [ ] 3.1.1.4 — `initial_balance = DecimalField(max_digits=14, decimal_places=2, default=0)`
    - [ ] 3.1.1.5 — `is_active = BooleanField(default=True)`
    - [ ] 3.1.1.6 — `created_at` e `updated_at`
  - [ ] 3.1.2 — Criar `class AccountType(models.TextChoices)` com: `CHECKING`, `SAVINGS`, `WALLET`, `INVESTMENT`
  - [ ] 3.1.3 — Criar method `get_current_balance()` que calcula saldo = `initial_balance` + receitas - despesas via ORM
  - [ ] 3.1.4 — Definir `__str__` retornando `self.name`
  - [ ] 3.1.5 — Definir `class Meta` com `ordering = ['name']`
  - [ ] 3.1.6 — Registrar no `admin.py` com `list_display` e `list_filter`

- [ ] **3.2 — Formulários (`accounts/forms.py`)**
  - [ ] 3.2.1 — Criar `AccountForm(ModelForm)` com campos: `name`, `account_type`, `initial_balance`
  - [ ] 3.2.2 — Aplicar classes CSS do design system nos widgets via `attrs`

- [ ] **3.3 — Views (`accounts/views.py`)**
  - [ ] 3.3.1 — Criar `AccountListView` (LoginRequiredMixin + ListView)
    - [ ] 3.3.1.1 — Filtrar queryset por `user=self.request.user`
    - [ ] 3.3.1.2 — Calcular e passar saldo total no contexto
  - [ ] 3.3.2 — Criar `AccountCreateView` (LoginRequiredMixin + CreateView)
    - [ ] 3.3.2.1 — Sobrescrever `form_valid()` para definir `form.instance.user = self.request.user`
    - [ ] 3.3.2.2 — Adicionar mensagem de sucesso
    - [ ] 3.3.2.3 — Redirecionar para lista de contas
  - [ ] 3.3.3 — Criar `AccountUpdateView` (LoginRequiredMixin + UpdateView)
    - [ ] 3.3.3.1 — Sobrescrever `get_queryset()` para filtrar por usuário
  - [ ] 3.3.4 — Criar `AccountDeleteView` (LoginRequiredMixin + DeleteView)
    - [ ] 3.3.4.1 — Sobrescrever `get_queryset()` para filtrar por usuário
    - [ ] 3.3.4.2 — Verificar se conta tem transações; se sim, negar exclusão com mensagem de erro

- [ ] **3.4 — URLs e Templates**
  - [ ] 3.4.1 — Criar `accounts/urls.py` com paths: list, create, update, delete
  - [ ] 3.4.2 — Criar `accounts/templates/accounts/account_list.html`
    - [ ] 3.4.2.1 — Herdar de `base_auth.html`
    - [ ] 3.4.2.2 — Card de saldo total no topo
    - [ ] 3.4.2.3 — Grid de cards para cada conta com: nome, tipo, saldo atual
    - [ ] 3.4.2.4 — Botão de adicionar conta
    - [ ] 3.4.2.5 — Botões de editar e excluir em cada card
    - [ ] 3.4.2.6 — Estado vazio (sem contas cadastradas) com CTA para criar
  - [ ] 3.4.3 — Criar `accounts/templates/accounts/account_form.html`
    - [ ] 3.4.3.1 — Formulário com design system (inputs, labels, botões)
    - [ ] 3.4.3.2 — Título dinâmico: "Nova Conta" ou "Editar Conta"
  - [ ] 3.4.4 — Criar `accounts/templates/accounts/account_confirm_delete.html`
    - [ ] 3.4.4.1 — Card de confirmação com mensagem e botões Cancelar / Excluir

- [ ] **3.5 — Migration**
  - [ ] 3.5.1 — Rodar `python manage.py makemigrations accounts`
  - [ ] 3.5.2 — Rodar `python manage.py migrate`
  - [ ] 3.5.3 — Testar CRUD completo via interface

---

### 🏷️ Sprint 4 — App `categories`: Categorias de Transações

**Objetivo:** CRUD de categorias com suporte a categorias padrão do sistema.

---

- [ ] **4.1 — Model `Category` (`categories/models.py`)**
  - [ ] 4.1.1 — Criar `class CategoryType(models.TextChoices)` com: `INCOME` (Receita), `EXPENSE` (Despesa)
  - [ ] 4.1.2 — Criar classe `Category` com os campos:
    - [ ] 4.1.2.1 — `user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE, null=True, blank=True)` (null = categoria do sistema)
    - [ ] 4.1.2.2 — `name = CharField(max_length=100)`
    - [ ] 4.1.2.3 — `category_type = CharField(max_length=10, choices=CategoryType.choices)`
    - [ ] 4.1.2.4 — `icon = CharField(max_length=10, blank=True)` (campo para emoji)
    - [ ] 4.1.2.5 — `is_default = BooleanField(default=False)` (categorias do sistema)
    - [ ] 4.1.2.6 — `created_at` e `updated_at`
  - [ ] 4.1.3 — Definir `class Meta` com `ordering = ['name']` e `unique_together = ['user', 'name', 'category_type']`
  - [ ] 4.1.4 — Registrar no `admin.py`

- [ ] **4.2 — Dados Iniciais (Categorias Padrão)**
  - [ ] 4.2.1 — Criar `categories/fixtures/default_categories.json` com categorias padrão
  - [ ] 4.2.2 — Categorias padrão de Despesa: Alimentação 🍔, Moradia 🏠, Transporte 🚗, Saúde 💊, Educação 📚, Lazer 🎮, Vestuário 👕, Outros 📦
  - [ ] 4.2.3 — Categorias padrão de Receita: Salário 💼, Freelance 💻, Investimentos 📈, Outros 💰
  - [ ] 4.2.4 — Documentar no README: `python manage.py loaddata default_categories`

- [ ] **4.3 — Formulários (`categories/forms.py`)**
  - [ ] 4.3.1 — Criar `CategoryForm(ModelForm)` com campos: `name`, `category_type`, `icon`
  - [ ] 4.3.2 — Aplicar classes CSS do design system nos widgets

- [ ] **4.4 — Views (`categories/views.py`)**
  - [ ] 4.4.1 — Criar `CategoryListView` (LoginRequiredMixin + ListView)
    - [ ] 4.4.1.1 — Listar: categorias do usuário + categorias padrão (user=None)
    - [ ] 4.4.1.2 — Separar na template: "Suas categorias" vs "Categorias do sistema"
  - [ ] 4.4.2 — Criar `CategoryCreateView` (LoginRequiredMixin + CreateView)
    - [ ] 4.4.2.1 — Definir `form.instance.user = self.request.user` no `form_valid()`
  - [ ] 4.4.3 — Criar `CategoryUpdateView` (LoginRequiredMixin + UpdateView)
    - [ ] 4.4.3.1 — Permitir editar somente categorias do próprio usuário
  - [ ] 4.4.4 — Criar `CategoryDeleteView` (LoginRequiredMixin + DeleteView)
    - [ ] 4.4.4.1 — Verificar se categoria tem transações; negar se houver
    - [ ] 4.4.4.2 — Bloquear exclusão de categorias padrão do sistema

- [ ] **4.5 — URLs e Templates**
  - [ ] 4.5.1 — Criar `categories/urls.py`
  - [ ] 4.5.2 — Criar `categories/templates/categories/category_list.html`
    - [ ] 4.5.2.1 — Seção de categorias do usuário com botões editar/excluir
    - [ ] 4.5.2.2 — Seção de categorias padrão (somente leitura, badge "Padrão")
    - [ ] 4.5.2.3 — Distinção visual por tipo: receita (emerald) vs despesa (rose)
  - [ ] 4.5.3 — Criar `categories/templates/categories/category_form.html`
  - [ ] 4.5.4 — Criar `categories/templates/categories/category_confirm_delete.html`

- [ ] **4.6 — Migration e Fixture**
  - [ ] 4.6.1 — Rodar `python manage.py makemigrations categories`
  - [ ] 4.6.2 — Rodar `python manage.py migrate`
  - [ ] 4.6.3 — Rodar `python manage.py loaddata default_categories`
  - [ ] 4.6.4 — Testar CRUD completo via interface

---

### 💸 Sprint 5 — App `transactions`: Movimentações Financeiras

**Objetivo:** CRUD completo de transações com filtros e atualização de saldo.

---

- [ ] **5.1 — Model `Transaction` (`transactions/models.py`)**
  - [ ] 5.1.1 — Criar `class TransactionType(models.TextChoices)` com: `INCOME` (Receita), `EXPENSE` (Despesa)
  - [ ] 5.1.2 — Criar classe `Transaction` com os campos:
    - [ ] 5.1.2.1 — `user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)`
    - [ ] 5.1.2.2 — `account = ForeignKey('accounts.Account', on_delete=PROTECT)`
    - [ ] 5.1.2.3 — `category = ForeignKey('categories.Category', on_delete=SET_NULL, null=True, blank=True)`
    - [ ] 5.1.2.4 — `transaction_type = CharField(max_length=10, choices=TransactionType.choices)`
    - [ ] 5.1.2.5 — `amount = DecimalField(max_digits=14, decimal_places=2)` (sempre positivo)
    - [ ] 5.1.2.6 — `description = CharField(max_length=300)`
    - [ ] 5.1.2.7 — `date = DateField()`
    - [ ] 5.1.2.8 — `notes = TextField(blank=True)`
    - [ ] 5.1.2.9 — `created_at` e `updated_at`
  - [ ] 5.1.3 — Definir `class Meta` com `ordering = ['-date', '-created_at']`
  - [ ] 5.1.4 — Definir `indexes` em `class Meta` para os campos `user`, `date`, `transaction_type`
  - [ ] 5.1.5 — Definir `__str__` retornando `f'{self.description} — {self.amount}'`
  - [ ] 5.1.6 — Registrar no `admin.py` com `list_display`, `list_filter`, `search_fields`

- [ ] **5.2 — Formulários (`transactions/forms.py`)**
  - [ ] 5.2.1 — Criar `TransactionForm(ModelForm)` com campos: `transaction_type`, `description`, `amount`, `date`, `account`, `category`, `notes`
  - [ ] 5.2.2 — No `__init__`, filtrar `account` e `category` para exibir somente as do usuário + categorias padrão
  - [ ] 5.2.3 — Configurar `date` com widget `DateInput(type='date')`
  - [ ] 5.2.4 — Validar que `amount > 0` no método `clean_amount()`
  - [ ] 5.2.5 — Aplicar classes CSS do design system nos widgets

- [ ] **5.3 — Views (`transactions/views.py`)**
  - [ ] 5.3.1 — Criar `TransactionListView` (LoginRequiredMixin + ListView)
    - [ ] 5.3.1.1 — Filtrar queryset por `user=self.request.user`
    - [ ] 5.3.1.2 — Aplicar filtro de mês/ano atual por padrão (via `GET` params)
    - [ ] 5.3.1.3 — Aceitar filtros via GET: `month`, `year`, `type`, `category`
    - [ ] 5.3.1.4 — Usar `select_related('account', 'category')` para evitar N+1
    - [ ] 5.3.1.5 — Calcular e passar no contexto: `total_income`, `total_expense`, `balance`
    - [ ] 5.3.1.6 — Passar lista de categorias do usuário no contexto (para o select de filtro)
  - [ ] 5.3.2 — Criar `TransactionCreateView` (LoginRequiredMixin + CreateView)
    - [ ] 5.3.2.1 — Passar `request.user` para o form no `get_form_kwargs()`
    - [ ] 5.3.2.2 — Definir `form.instance.user = self.request.user` no `form_valid()`
    - [ ] 5.3.2.3 — Adicionar mensagem de sucesso
  - [ ] 5.3.3 — Criar `TransactionUpdateView` (LoginRequiredMixin + UpdateView)
    - [ ] 5.3.3.1 — Filtrar queryset por usuário
    - [ ] 5.3.3.2 — Passar `request.user` para o form
  - [ ] 5.3.4 — Criar `TransactionDeleteView` (LoginRequiredMixin + DeleteView)
    - [ ] 5.3.4.1 — Filtrar queryset por usuário
    - [ ] 5.3.4.2 — Adicionar mensagem de sucesso após exclusão

- [ ] **5.4 — URLs e Templates**
  - [ ] 5.4.1 — Criar `transactions/urls.py` com paths: list, create, update, delete
  - [ ] 5.4.2 — Criar `transactions/templates/transactions/transaction_list.html`
    - [ ] 5.4.2.1 — Herdar de `base_auth.html`
    - [ ] 5.4.2.2 — Cards de resumo: Total Receitas (emerald), Total Despesas (rose), Saldo (violet ou emerald/rose conforme positivo/negativo)
    - [ ] 5.4.2.3 — Barra de filtros (form GET): seletor de mês/ano, tipo, categoria
    - [ ] 5.4.2.4 — Tabela de transações com: data, descrição, categoria, conta, valor (colorido por tipo)
    - [ ] 5.4.2.5 — Botões editar e excluir por linha
    - [ ] 5.4.2.6 — Botão "Nova Transação" destacado
    - [ ] 5.4.2.7 — Estado vazio (sem transações) com CTA
    - [ ] 5.4.2.8 — Badge de tipo (Receita/Despesa) por linha
  - [ ] 5.4.3 — Criar `transactions/templates/transactions/transaction_form.html`
    - [ ] 5.4.3.1 — Campos do formulário com design system
    - [ ] 5.4.3.2 — Título dinâmico: "Nova Transação" ou "Editar Transação"
  - [ ] 5.4.4 — Criar `transactions/templates/transactions/transaction_confirm_delete.html`

- [ ] **5.5 — Migration**
  - [ ] 5.5.1 — Rodar `python manage.py makemigrations transactions`
  - [ ] 5.5.2 — Rodar `python manage.py migrate`
  - [ ] 5.5.3 — Testar CRUD completo: criar receita, criar despesa, editar, excluir
  - [ ] 5.5.4 — Verificar que filtros funcionam corretamente

---

### 📊 Sprint 6 — Dashboard Principal

**Objetivo:** Implementar dashboard com resumo financeiro do mês atual.

---

- [ ] **6.1 — View do Dashboard**
  - [ ] 6.1.1 — Criar `DashboardView` (LoginRequiredMixin + TemplateView) em arquivo `views.py` na raiz ou em app dedicada
  - [ ] 6.1.2 — Calcular no contexto: `total_income` (receitas do mês), `total_expense` (despesas do mês), `balance` (diferença)
  - [ ] 6.1.3 — Consultar últimas 5 transações com `select_related`
  - [ ] 6.1.4 — Consultar todas as contas ativas do usuário com saldo atual
  - [ ] 6.1.5 — Filtrar dados pelo mês e ano atual usando `date__month` e `date__year`

- [ ] **6.2 — URL do Dashboard**
  - [ ] 6.2.1 — Adicionar em `core/urls.py`: `path('dashboard/', DashboardView.as_view(), name='dashboard')`
  - [ ] 6.2.2 — Configurar `LOGIN_REDIRECT_URL = '/dashboard/'` no `settings.py`

- [ ] **6.3 — Template do Dashboard**
  - [ ] 6.3.1 — Criar `templates/dashboard.html` herdando de `base_auth.html`
  - [ ] 6.3.2 — Implementar header com: título "Dashboard", período atual e saudação ao usuário
  - [ ] 6.3.3 — Grid de 3 cards de métricas: Receitas (emerald), Despesas (rose), Saldo do mês (violet)
  - [ ] 6.3.4 — Seção "Últimas Transações": tabela compacta com as 5 mais recentes e link para ver todas
  - [ ] 6.3.5 — Seção "Minhas Contas": lista de contas com saldo atual e link para gerenciar
  - [ ] 6.3.6 — Estado vazio: mensagens CTA quando não há contas ou transações

- [ ] **6.4 — Testes Manuais do Dashboard**
  - [ ] 6.4.1 — Verificar que usuário sem dados vê o dashboard com mensagens de boas-vindas
  - [ ] 6.4.2 — Verificar cálculos de receita, despesa e saldo com dados reais
  - [ ] 6.4.3 — Verificar links de ação que levam às seções corretas

---

### 🎨 Sprint 7 — Refinamento Visual e UX

**Objetivo:** Polir o design system, consistência visual e experiência do usuário.

---

- [ ] **7.1 — Consistência do Design System**
  - [ ] 7.1.1 — Revisar todos os templates e garantir herança correta de `base_auth.html` ou `base.html`
  - [ ] 7.1.2 — Garantir que todos os inputs seguem o padrão de classes do design system
  - [ ] 7.1.3 — Garantir que todos os botões seguem os padrões documentados (primário, secundário, perigo)
  - [ ] 7.1.4 — Garantir que mensagens Django Messages são renderizadas corretamente em todos os fluxos
  - [ ] 7.1.5 — Verificar active state da sidebar em todas as páginas

- [ ] **7.2 — Responsividade Mobile**
  - [ ] 7.2.1 — Testar sidebar em viewport mobile (deve colapsar ou virar menu hamburguer)
  - [ ] 7.2.2 — Verificar grid de cards no dashboard em mobile (1 coluna)
  - [ ] 7.2.3 — Verificar tabela de transações em mobile (scroll horizontal)
  - [ ] 7.2.4 — Verificar formulários em mobile (campo fullwidth, botões fullwidth)

- [ ] **7.3 — Tratamento de Erros e Edge Cases**
  - [ ] 7.3.1 — Criar template `templates/404.html` com design system
  - [ ] 7.3.2 — Criar template `templates/500.html` com design system
  - [ ] 7.3.3 — Verificar mensagem de erro ao tentar excluir conta com transações
  - [ ] 7.3.4 — Verificar mensagem de erro ao tentar excluir categoria com transações
  - [ ] 7.3.5 — Verificar redirect para login ao tentar acessar URL protegida sem autenticação

- [ ] **7.4 — Revisão Final de Código**
  - [ ] 7.4.1 — Verificar conformidade PEP 8 em todos os arquivos Python
  - [ ] 7.4.2 — Garantir uso de aspas simples em todo código Python
  - [ ] 7.4.3 — Garantir que nenhum model está sem `created_at` e `updated_at`
  - [ ] 7.4.4 — Verificar que todas as queries filtram por `user=request.user`
  - [ ] 7.4.5 — Remover imports não utilizados
  - [ ] 7.4.6 — Revisar `admin.py` de todos os apps para configuração adequada

---

### 🔒 Sprint 8 — Segurança e Produção (Futuro)

**Objetivo:** Preparar para ambiente de produção. *(Não implementar no MVP)*

---

- [ ] **8.1 — Variáveis de Ambiente**
  - [ ] 8.1.1 — Instalar `python-decouple`
  - [ ] 8.1.2 — Mover `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS` para `.env`
  - [ ] 8.1.3 — Criar `.env.example` documentado

- [ ] **8.2 — Banco de Dados PostgreSQL**
  - [ ] 8.2.1 — Instalar `psycopg2-binary`
  - [ ] 8.2.2 — Configurar `DATABASES` via variável de ambiente
  - [ ] 8.2.3 — Testar migração de SQLite para PostgreSQL

- [ ] **8.3 — Arquivos Estáticos em Produção**
  - [ ] 8.3.1 — Instalar e configurar `whitenoise`
  - [ ] 8.3.2 — Configurar TailwindCSS com build de produção (purge de classes)
  - [ ] 8.3.3 — Rodar `python manage.py collectstatic`

- [ ] **8.4 — Docker**
  - [ ] 8.4.1 — Criar `Dockerfile`
  - [ ] 8.4.2 — Criar `docker-compose.yml` (app + banco)
  - [ ] 8.4.3 — Testar build e execução via Docker

---

### 🧪 Sprint 9 — Testes (Futuro)

**Objetivo:** Cobertura de testes automatizados. *(Não implementar no MVP)*

---

- [ ] **9.1 — Configuração de Testes**
  - [ ] 9.1.1 — Instalar `pytest-django` e `factory-boy`
  - [ ] 9.1.2 — Configurar `pytest.ini`

- [ ] **9.2 — Testes de Models**
  - [ ] 9.2.1 — Testes para `CustomUser`
  - [ ] 9.2.2 — Testes para `Account.get_current_balance()`
  - [ ] 9.2.3 — Testes para `Transaction`

- [ ] **9.3 — Testes de Views**
  - [ ] 9.3.1 — Testes de autenticação (register, login, logout)
  - [ ] 9.3.2 — Testes de CRUD de contas
  - [ ] 9.3.3 — Testes de CRUD de transações
  - [ ] 9.3.4 — Testes de isolamento de dados entre usuários