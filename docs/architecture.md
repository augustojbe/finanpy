# Arquitetura — Estrutura do Projeto

## Visão geral

O Finanpy organiza suas responsabilidades em **apps Django isoladas**, cada uma
com um domínio funcional bem definido. A pasta `core` concentra as configurações
globais do projeto.

---

## Estrutura de diretórios

```
finanpy/
├── accounts/        # Contas bancárias do usuário
├── categories/      # Categorias de transações
├── core/            # Configurações globais do projeto
├── profiles/        # Perfil de cada usuário
├── transactions/    # Transações financeiras (receitas e despesas)
├── users/           # Modelo de usuário e autenticação
├── docs/            # Documentação do projeto
├── db.sqlite3       # Banco de dados SQLite
├── manage.py        # Entry point do Django
├── prd.md           # Product Requirements Document
└── requirements.txt # Dependências Python
```

---

## Apps e responsabilidades

### `core`
Configurações globais do projeto Django.

| Arquivo | Função |
|---|---|
| `settings.py` | Configurações da aplicação (banco, apps, middleware, etc.) |
| `urls.py` | Roteamento raiz — inclui as URLs de cada app |
| `wsgi.py` | Entry point WSGI para deploy |
| `asgi.py` | Entry point ASGI para deploy |

---

### `users`
Modelo de usuário e autenticação.

- Responsável pelo modelo `CustomUser`, que herda de `AbstractUser`.
- O login é feito via **e-mail**, não via username.
- Contém o backend de autenticação por e-mail (`backends.py`).
- Gerencia as views de landing page, registro, login e logout.

---

### `profiles`
Perfil complementar de cada usuário.

- Cada usuário possui exatamente um perfil (`OneToOneField`).
- O perfil é criado automaticamente via **signal** (`post_save` no `CustomUser`).
- O signal fica em `profiles/signals.py`, registrado no `ProfilesConfig.ready()`.

---

### `accounts`
Contas bancárias do usuário.

- Representa fontes de dinheiro: conta corrente, poupança, carteira, investimento.
- Cada conta pertence a um único usuário.
- O saldo atual de uma conta é calculado a partir do saldo inicial + transações.

---

### `categories`
Categorias para classificar transações.

- Existem **categorias padrão do sistema** (sem usuário vinculado) e categorias
  personalizadas criadas pelo próprio usuário.
- Tipos de categoria: `Receita` ou `Despesa`.

---

### `transactions`
Transações financeiras.

- Registra receitas e despesas do usuário.
- Cada transação está vinculada a uma conta e a uma categoria.
- Tipos de transação: `Receita` ou `Despesa`.

---

## Campos obrigatórios em todos os models

Todo model do projeto deve ter os seguintes campos:

```python
created_at = models.DateTimeField(auto_now_add=True)
updated_at = models.DateTimeField(auto_now=True)
```

---

## Configurações relevantes (`core/settings.py`)

| Configuração | Valor atual | Observação |
|---|---|---|
| `DEBUG` | `True` | Desativar em produção |
| `DATABASES` | SQLite | `db.sqlite3` na raiz |
| `LANGUAGE_CODE` | `en-us` | Alterar para `pt-br` |
| `TIME_ZONE` | `UTC` | Alterar para `America/Sao_Paulo` |
| `INSTALLED_APPS` | 5 apps customizadas | `accounts`, `categories`, `profiles`, `transactions`, `users` |

> ⚠️ `AUTH_USER_MODEL` deve ser configurado para `'users.CustomUser'`
> **antes** da primeira migration. Alterar após as migrations iniciais requer
> reset completo do banco.

---

## Roteamento

O arquivo `core/urls.py` é o roteador raiz. Cada app expõe seu próprio
`urls.py` e é incluída aqui via `include()`.

```
/                     → landing page (users)
/cadastro/            → registro (users)
/entrar/              → login (users)
/sair/                → logout (users)
/dashboard/           → dashboard principal
/contas/              → app accounts
/categorias/          → app categories
/transacoes/          → app transactions
/perfil/              → app profiles
/admin/               → Django Admin
```

---

## Autenticação

- Sistema nativo do Django (`django.contrib.auth`).
- Login via **e-mail** ao invés de username (backend customizado em `users/backends.py`).
- Rotas protegidas usam `LoginRequiredMixin` nas Class-Based Views.
- Configurações relevantes no `settings.py`:
  - `LOGIN_URL` — redireciona usuários não autenticados
  - `LOGIN_REDIRECT_URL` — destino após login bem-sucedido
  - `LOGOUT_REDIRECT_URL` — destino após logout
