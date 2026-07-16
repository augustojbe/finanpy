# Finanpy — Product Requirements Document (PRD)

> **Versão:** 1.0.0 · **Status:** Aprovado para Desenvolvimento · **Data:** 2026-07-15

---

## 1. Visão Geral

**Finanpy** é um sistema web de gestão de finanças pessoais desenvolvido com
Python e Django (full stack), com interface moderna, responsiva e em português
brasileiro. O sistema permite que usuários registrem e acompanhem suas
movimentações financeiras — receitas, despesas e transferências — organizadas
por categorias e contas bancárias.

O projeto segue uma filosofia de **simplicidade e coesão**: sem over-engineering,
sem dependências desnecessárias, usando ao máximo os recursos nativos do Django
e SQLite como banco de dados.

---

## 2. Sobre o Produto

| Atributo          | Valor                                            |
|-------------------|--------------------------------------------------|
| **Nome**          | Finanpy                                          |
| **Tipo**          | Aplicação Web (Django Full Stack)                |
| **Frontend**      | Django Template Language + TailwindCSS           |
| **Backend**       | Python + Django                                  |
| **Banco de Dados**| SQLite (padrão Django)                           |
| **Autenticação**  | Sistema nativo Django (login via e-mail)         |
| **Idioma da UI**  | Português Brasileiro                             |
| **Idioma do código** | Inglês                                        |
| **Estilo de código** | PEP 8, aspas simples, Class-Based Views       |

---

## 3. Propósito

Oferecer uma ferramenta **simples, visualmente agradável e funcional** para que
pessoas físicas possam:

- Registrar suas receitas e despesas do dia a dia.
- Organizar movimentações por categorias e contas bancárias.
- Ter uma visão clara do seu saldo e fluxo de caixa mensal.
- Tomar decisões financeiras mais conscientes com base em dados históricos.

O Finanpy não pretende ser um ERP financeiro. Seu diferencial é a **leveza,
clareza e facilidade de uso**.

---

## 4. Público-Alvo

| Perfil              | Descrição                                                      |
|---------------------|----------------------------------------------------------------|
| **Primário**        | Pessoas físicas que querem controlar gastos pessoais           |
| **Secundário**      | Freelancers e autônomos com renda variável                     |
| **Terciário**       | Desenvolvedores que querem estudar Django full stack na prática|

**Características comuns do usuário:**
- Usa smartphone e computador.
- Não é necessariamente técnico.
- Quer simplicidade: registro rápido e visualização clara.
- Valoriza design limpo e moderno.

---

## 5. Objetivos

### 5.1 Objetivos de Produto

- Entregar um MVP funcional com autenticação, contas, categorias e transações.
- Interface com design system consistente em todas as telas.
- Sistema 100% operacional com Django nativo + SQLite, sem dependências externas complexas.

### 5.2 Objetivos de Negócio

- Ser uma base de código de referência para sistemas Django full stack.
- Estar pronto para escalonamento futuro (PostgreSQL, Docker, API REST).

### 5.3 Objetivos Técnicos

- Separação clara de responsabilidades via apps Django.
- Código limpo, em inglês, seguindo PEP 8.
- Zero dívida técnica estrutural no MVP.

---

## 6. Requisitos Funcionais

### 6.1 Módulo: Site Público (Landing Page)

| ID     | Requisito                                                           | Prioridade |
|--------|---------------------------------------------------------------------|------------|
| RF-001 | Página inicial pública de apresentação do sistema                   | Must Have  |
| RF-002 | Botão "Cadastre-se" na landing page                                 | Must Have  |
| RF-003 | Botão "Entrar" na landing page                                      | Must Have  |

### 6.2 Módulo: Autenticação (users)

| ID     | Requisito                                                           | Prioridade |
|--------|---------------------------------------------------------------------|------------|
| RF-010 | Cadastro de novo usuário com e-mail, nome e senha                   | Must Have  |
| RF-011 | Login com e-mail e senha (não username)                             | Must Have  |
| RF-012 | Logout                                                              | Must Have  |
| RF-013 | Validação de e-mail único no cadastro                               | Must Have  |
| RF-014 | Validação de força de senha (mínimo 8 caracteres)                   | Must Have  |
| RF-015 | Redirecionamento para dashboard após login bem-sucedido             | Must Have  |
| RF-016 | Proteção de rotas autenticadas (redirect para login se não logado)  | Must Have  |

### 6.3 Módulo: Perfil (profiles)

| ID     | Requisito                                                           | Prioridade |
|--------|---------------------------------------------------------------------|------------|
| RF-020 | Criação automática de perfil ao registrar usuário (via signal)      | Must Have  |
| RF-021 | Visualização e edição de dados do perfil (nome, e-mail)             | Must Have  |
| RF-022 | Alteração de senha                                                  | Must Have  |

### 6.4 Módulo: Contas Bancárias (accounts)

| ID     | Requisito                                                           | Prioridade |
|--------|---------------------------------------------------------------------|------------|
| RF-030 | Listar contas do usuário autenticado                                | Must Have  |
| RF-031 | Criar nova conta (nome, tipo, saldo inicial)                        | Must Have  |
| RF-032 | Editar conta existente                                              | Must Have  |
| RF-033 | Excluir conta (somente se sem transações vinculadas)                | Must Have  |
| RF-034 | Exibir saldo atual calculado de cada conta                          | Must Have  |
| RF-035 | Tipos de conta: Corrente, Poupança, Carteira, Investimento          | Must Have  |

### 6.5 Módulo: Categorias (categories)

| ID     | Requisito                                                           | Prioridade |
|--------|---------------------------------------------------------------------|------------|
| RF-040 | Categorias padrão do sistema (pré-cadastradas via fixture/migration)| Must Have  |
| RF-041 | Listar categorias do usuário + categorias padrão                    | Must Have  |
| RF-042 | Criar categoria personalizada (nome, tipo: receita/despesa, ícone)  | Must Have  |
| RF-043 | Editar categoria personalizada                                      | Must Have  |
| RF-044 | Excluir categoria personalizada (somente sem transações vinculadas) | Must Have  |

### 6.6 Módulo: Transações (transactions)

| ID     | Requisito                                                           | Prioridade |
|--------|---------------------------------------------------------------------|------------|
| RF-050 | Listar transações do usuário com filtro por mês/ano atual           | Must Have  |
| RF-051 | Registrar transação do tipo Receita                                 | Must Have  |
| RF-052 | Registrar transação do tipo Despesa                                 | Must Have  |
| RF-053 | Campos da transação: descrição, valor, data, conta, categoria, tipo | Must Have  |
| RF-054 | Editar transação existente                                          | Must Have  |
| RF-055 | Excluir transação                                                   | Must Have  |
| RF-056 | Filtrar transações por: mês, tipo (receita/despesa), categoria      | Must Have  |
| RF-057 | Exibir total de receitas, total de despesas e saldo do período      | Must Have  |

### 6.7 Módulo: Dashboard

| ID     | Requisito                                                           | Prioridade |
|--------|---------------------------------------------------------------------|------------|
| RF-060 | Dashboard pós-login com resumo financeiro do mês atual              | Must Have  |
| RF-061 | Cards com: Total de Receitas, Total de Despesas, Saldo do mês       | Must Have  |
| RF-062 | Lista das 5 últimas transações                                      | Must Have  |
| RF-063 | Lista de contas com seus saldos                                     | Must Have  |

---

### 6.8 Fluxograma de UX

```mermaid
flowchart TD
    A([Usuário acessa o sistema]) --> B{Autenticado?}
    B -- Não --> C[Landing Page Pública]
    C --> D{Escolha}
    D -- Cadastre-se --> E[Formulário de Registro]
    E --> F{Dados válidos?}
    F -- Não --> E
    F -- Sim --> G[Cria usuário + perfil via signal]
    G --> H[Dashboard Principal]
    D -- Entrar --> I[Formulário de Login e-mail + senha]
    I --> J{Credenciais válidas?}
    J -- Não --> I
    J -- Sim --> H
    B -- Sim --> H

    H --> K{O que deseja fazer?}

    K -- Gerenciar Contas --> L[Lista de Contas]
    L --> L1[Criar Conta]
    L --> L2[Editar Conta]
    L --> L3[Excluir Conta]

    K -- Gerenciar Categorias --> M[Lista de Categorias]
    M --> M1[Criar Categoria]
    M --> M2[Editar Categoria]
    M --> M3[Excluir Categoria]

    K -- Gerenciar Transações --> N[Lista de Transações]
    N --> N1[Criar Transação]
    N --> N2[Editar Transação]
    N --> N3[Excluir Transação]
    N --> N4[Filtrar por Período / Tipo / Categoria]

    K -- Perfil --> O[Visualizar / Editar Perfil]
    O --> O1[Alterar dados pessoais]
    O --> O2[Alterar senha]

    K -- Sair --> P[Logout]
    P --> C
```

---

## 7. Requisitos Não-Funcionais

| ID      | Categoria          | Requisito                                                                        |
|---------|--------------------|----------------------------------------------------------------------------------|
| RNF-001 | **Segurança**      | Senhas armazenadas com hashing PBKDF2 (padrão Django)                            |
| RNF-002 | **Segurança**      | CSRF protection em todos os formulários (middleware padrão Django)               |
| RNF-003 | **Segurança**      | Rotas autenticadas protegidas com `LoginRequiredMixin`                           |
| RNF-004 | **Segurança**      | Dados de um usuário jamais acessíveis por outro (FK obrigatória em todos os models) |
| RNF-005 | **Performance**    | Listagem de transações com tempo de resposta < 500ms para até 5.000 registros   |
| RNF-006 | **Performance**    | Índices de banco nos campos `user`, `date` e `type` em transactions             |
| RNF-007 | **Usabilidade**    | Interface 100% responsiva (mobile-first com TailwindCSS)                        |
| RNF-008 | **Manutenibilidade**| Código em inglês, PEP 8, aspas simples, sem lógica de negócio em templates     |
| RNF-009 | **Escalabilidade** | Banco substituível de SQLite para PostgreSQL sem mudança de código de aplicação |
| RNF-010 | **Simplicidade**   | Sem over-engineering: sem Celery, Redis, DRF ou libs desnecessárias no MVP      |
| RNF-011 | **Consistência**   | Design system único aplicado em 100% das telas via template base                |
| RNF-012 | **Internacionalização** | Toda UI em português brasileiro; código-fonte em inglês                   |

---

## 8. Arquitetura Técnica

### 8.1 Stack

| Camada           | Tecnologia                                  |
|------------------|---------------------------------------------|
| Linguagem        | Python 3.12+                                |
| Framework Web    | Django 6.x                                  |
| Template Engine  | Django Template Language (DTL)              |
| CSS Framework    | TailwindCSS (via CDN no desenvolvimento)    |
| Banco de Dados   | SQLite (padrão Django)                      |
| Autenticação     | Django Auth nativo (customizado para e-mail)|
| ORM              | Django ORM                                  |
| Views            | Class-Based Views (CBV) preferencialmente   |
| Signals          | Django Signals (arquivo `signals.py` por app)|

### 8.2 Estrutura de Diretórios

```
finanpy/
├── accounts/           # Contas bancárias do usuário
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── templates/
│       └── accounts/
├── categories/         # Categorias de transações
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── templates/
│       └── categories/
├── core/               # Configurações globais
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── profiles/           # Perfil de usuário
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── signals.py      # Signal post_save para criar perfil
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── templates/
│       └── profiles/
├── transactions/       # Transações financeiras
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── templates/
│       └── transactions/
├── users/              # Modelo de usuário customizado
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── backends.py     # Backend de autenticação por e-mail
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── templates/
│       └── users/
├── templates/          # Templates globais e base
│   ├── base.html
│   ├── dashboard.html
│   └── landing.html
├── static/             # Arquivos estáticos globais
├── db.sqlite3
├── manage.py
├── requirements.txt
└── prd.md
```

### 8.3 Estrutura de Dados — Schemas (Mermaid ERD)

```mermaid
erDiagram
    USER {
        int id PK
        string email UK
        string first_name
        string last_name
        string password
        bool is_active
        bool is_staff
        datetime date_joined
        datetime created_at
        datetime updated_at
    }

    PROFILE {
        int id PK
        int user_id FK
        string phone
        datetime created_at
        datetime updated_at
    }

    ACCOUNT {
        int id PK
        int user_id FK
        string name
        string account_type
        decimal initial_balance
        decimal current_balance
        bool is_active
        datetime created_at
        datetime updated_at
    }

    CATEGORY {
        int id PK
        int user_id FK "NULL = categoria do sistema"
        string name
        string category_type
        string icon
        bool is_default
        datetime created_at
        datetime updated_at
    }

    TRANSACTION {
        int id PK
        int user_id FK
        int account_id FK
        int category_id FK
        string transaction_type
        decimal amount
        string description
        date date
        string notes
        datetime created_at
        datetime updated_at
    }

    USER ||--o| PROFILE : "tem um"
    USER ||--o{ ACCOUNT : "possui"
    USER ||--o{ CATEGORY : "cria"
    USER ||--o{ TRANSACTION : "registra"
    ACCOUNT ||--o{ TRANSACTION : "recebe"
    CATEGORY ||--o{ TRANSACTION : "classifica"
```

### 8.4 Fluxo de Dados por Request

```mermaid
sequenceDiagram
    participant U as Usuário (Browser)
    participant V as View (CBV Django)
    participant F as Form (Django Form)
    participant M as Model (ORM)
    participant DB as SQLite

    U->>V: HTTP Request (POST/GET)
    V->>V: Verifica autenticação (LoginRequiredMixin)
    V->>F: Instancia form com request.POST
    F->>F: Valida dados
    alt Dados inválidos
        F-->>V: Erros de validação
        V-->>U: Re-renderiza template com erros
    else Dados válidos
        F-->>V: Dados limpos (cleaned_data)
        V->>M: Cria/Atualiza/Deleta objeto
        M->>DB: SQL via ORM
        DB-->>M: Resultado
        M-->>V: Objeto salvo
        V-->>U: Redirect com mensagem de sucesso
    end
```

---

## 9. Design System

### 9.1 Visão Geral

Design **dark mode** com gradientes vibrantes, tipografia moderna e componentes
consistentes em todas as telas. Implementado 100% com TailwindCSS dentro do
Django Template Language.

### 9.2 Paleta de Cores

| Papel               | Token TailwindCSS             | Hex        | Uso                                  |
|---------------------|-------------------------------|------------|--------------------------------------|
| **Fundo Principal** | `bg-gray-950`                 | `#030712`  | Fundo global da aplicação            |
| **Fundo Card**      | `bg-gray-900`                 | `#111827`  | Cards, painéis, formulários          |
| **Fundo Elevado**   | `bg-gray-800`                 | `#1f2937`  | Inputs, tabelas, hover states        |
| **Borda**           | `border-gray-700`             | `#374151`  | Bordas de cards, inputs              |
| **Primária**        | `from-violet-600 to-indigo-600` | Gradiente | Botões primários, acentos            |
| **Primária hover**  | `from-violet-500 to-indigo-500` | Gradiente | Estado hover do primário             |
| **Receita**         | `text-emerald-400`            | `#34d399`  | Valores positivos, receitas          |
| **Despesa**         | `text-rose-400`               | `#fb7185`  | Valores negativos, despesas          |
| **Neutro**          | `text-gray-400`               | `#9ca3af`  | Textos secundários, labels           |
| **Texto Principal** | `text-white`                  | `#ffffff`  | Títulos, valores principais          |
| **Texto Secundário**| `text-gray-300`               | `#d1d5db`  | Textos de apoio                      |
| **Destaque/Accent** | `text-violet-400`             | `#a78bfa`  | Links, ícones de destaque            |

### 9.3 Tipografia

```html
<!-- Fonte via Google Fonts no base.html -->
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">

<!-- Aplicação no body -->
<body class="font-['Inter'] bg-gray-950 text-white antialiased">
```

| Elemento          | Classes TailwindCSS                              |
|-------------------|--------------------------------------------------|
| H1 (Página)       | `text-3xl font-bold text-white`                  |
| H2 (Seção)        | `text-xl font-semibold text-white`               |
| H3 (Card)         | `text-lg font-medium text-gray-100`              |
| Texto corpo       | `text-sm text-gray-300`                          |
| Label de form     | `text-sm font-medium text-gray-400`              |
| Valor monetário   | `text-2xl font-bold tabular-nums`                |
| Badge / Tag       | `text-xs font-medium`                            |

### 9.4 Gradiente de Fundo (Header e Landing)

```html
<!-- Fundo com gradiente para seções de destaque -->
<div class="bg-gradient-to-br from-gray-950 via-gray-900 to-violet-950">

<!-- Gradiente no logo/brand -->
<span class="bg-gradient-to-r from-violet-400 to-indigo-400 bg-clip-text text-transparent font-bold text-2xl">
    Finanpy
</span>
```

### 9.5 Botões

```html
<!-- Botão Primário -->
<button class="w-full bg-gradient-to-r from-violet-600 to-indigo-600
               hover:from-violet-500 hover:to-indigo-500
               text-white font-semibold py-2.5 px-6 rounded-lg
               transition-all duration-200 ease-in-out
               focus:outline-none focus:ring-2 focus:ring-violet-500 focus:ring-offset-2 focus:ring-offset-gray-900
               disabled:opacity-50 disabled:cursor-not-allowed">
    Salvar
</button>

<!-- Botão Secundário / Outline -->
<button class="border border-gray-600 hover:border-gray-500
               text-gray-300 hover:text-white
               font-medium py-2.5 px-6 rounded-lg
               transition-all duration-200
               hover:bg-gray-800">
    Cancelar
</button>

<!-- Botão de Perigo (excluir) -->
<button class="bg-rose-600 hover:bg-rose-500
               text-white font-medium py-2 px-4 rounded-lg
               transition-colors duration-200">
    Excluir
</button>

<!-- Botão Ícone -->
<button class="p-2 rounded-lg text-gray-400 hover:text-white hover:bg-gray-700
               transition-colors duration-200">
    <!-- ícone SVG aqui -->
</button>
```

### 9.6 Inputs e Formulários

```html
<!-- Estrutura de campo de formulário -->
<div class="space-y-1">
    <label for="email" class="block text-sm font-medium text-gray-400">
        E-mail
    </label>
    <input
        type="email"
        id="email"
        name="email"
        class="w-full bg-gray-800 border border-gray-700
               text-white placeholder-gray-500
               rounded-lg px-4 py-2.5
               focus:outline-none focus:ring-2 focus:ring-violet-500 focus:border-transparent
               transition-all duration-200"
        placeholder="seu@email.com"
    >
    <!-- Mensagem de erro -->
    <p class="text-xs text-rose-400">Campo obrigatório.</p>
</div>

<!-- Select -->
<select class="w-full bg-gray-800 border border-gray-700
               text-white rounded-lg px-4 py-2.5
               focus:outline-none focus:ring-2 focus:ring-violet-500 focus:border-transparent">
    <option>Selecione...</option>
</select>

<!-- Textarea -->
<textarea class="w-full bg-gray-800 border border-gray-700
                 text-white placeholder-gray-500
                 rounded-lg px-4 py-2.5 resize-none
                 focus:outline-none focus:ring-2 focus:ring-violet-500 focus:border-transparent"
          rows="3"></textarea>
```

### 9.7 Cards

```html
<!-- Card padrão -->
<div class="bg-gray-900 border border-gray-800 rounded-xl p-6
            hover:border-gray-700 transition-colors duration-200">
    <!-- conteúdo -->
</div>

<!-- Card de métrica (Dashboard) -->
<div class="bg-gray-900 border border-gray-800 rounded-xl p-6">
    <div class="flex items-center justify-between mb-2">
        <span class="text-sm text-gray-400">Total de Receitas</span>
        <span class="p-2 bg-emerald-500/10 rounded-lg text-emerald-400">
            <!-- ícone -->
        </span>
    </div>
    <p class="text-2xl font-bold text-emerald-400 tabular-nums">R$ 5.200,00</p>
    <p class="text-xs text-gray-500 mt-1">Mês atual</p>
</div>
```

### 9.8 Tabelas

```html
<div class="overflow-x-auto rounded-xl border border-gray-800">
    <table class="w-full text-sm">
        <thead class="bg-gray-800/50">
            <tr>
                <th class="text-left text-gray-400 font-medium px-6 py-4">Descrição</th>
                <th class="text-left text-gray-400 font-medium px-6 py-4">Data</th>
                <th class="text-right text-gray-400 font-medium px-6 py-4">Valor</th>
            </tr>
        </thead>
        <tbody class="divide-y divide-gray-800">
            <tr class="hover:bg-gray-800/30 transition-colors duration-150">
                <td class="px-6 py-4 text-gray-200">Mercado</td>
                <td class="px-6 py-4 text-gray-400">15/07/2026</td>
                <td class="px-6 py-4 text-right font-semibold text-rose-400">- R$ 150,00</td>
            </tr>
        </tbody>
    </table>
</div>
```

### 9.9 Layout e Grid

```html
<!-- Layout principal pós-login -->
<div class="min-h-screen bg-gray-950 flex">
    <!-- Sidebar -->
    <aside class="w-64 bg-gray-900 border-r border-gray-800 flex flex-col">
        <!-- nav links -->
    </aside>
    <!-- Conteúdo principal -->
    <main class="flex-1 overflow-y-auto">
        <div class="p-8 max-w-7xl mx-auto">
            <!-- conteúdo da página -->
        </div>
    </main>
</div>

<!-- Grid de cards (Dashboard) -->
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
    <!-- cards -->
</div>
```

### 9.10 Navegação (Sidebar)

```html
<aside class="w-64 bg-gray-900 border-r border-gray-800 flex flex-col min-h-screen">
    <!-- Logo -->
    <div class="px-6 py-5 border-b border-gray-800">
        <span class="bg-gradient-to-r from-violet-400 to-indigo-400
                     bg-clip-text text-transparent font-bold text-xl">
            Finanpy
        </span>
    </div>
    <!-- Links de navegação -->
    <nav class="flex-1 px-4 py-6 space-y-1">
        <a href="{% url 'dashboard' %}"
           class="flex items-center gap-3 px-4 py-2.5 rounded-lg
                  text-gray-400 hover:text-white hover:bg-gray-800
                  transition-colors duration-200
                  {% if request.resolver_match.url_name == 'dashboard' %}
                      bg-violet-600/20 text-violet-400 border border-violet-600/30
                  {% endif %}">
            <!-- ícone + texto -->
            <span>Dashboard</span>
        </a>
    </nav>
    <!-- Footer da sidebar: usuário logado -->
    <div class="px-4 py-4 border-t border-gray-800">
        <div class="flex items-center gap-3">
            <div class="w-8 h-8 rounded-full bg-gradient-to-br from-violet-500 to-indigo-500
                        flex items-center justify-center text-white text-sm font-semibold">
                {{ request.user.first_name.0 }}
            </div>
            <div class="flex-1 min-w-0">
                <p class="text-sm font-medium text-white truncate">{{ request.user.get_full_name }}</p>
                <p class="text-xs text-gray-500 truncate">{{ request.user.email }}</p>
            </div>
        </div>
    </div>
</aside>
```

### 9.11 Alertas / Mensagens (Django Messages)

```html
<!-- Sucesso -->
<div class="bg-emerald-500/10 border border-emerald-500/30 text-emerald-400
            px-4 py-3 rounded-lg text-sm flex items-center gap-2">
    <!-- ícone check --> Operação realizada com sucesso!
</div>
<!-- Erro -->
<div class="bg-rose-500/10 border border-rose-500/30 text-rose-400
            px-4 py-3 rounded-lg text-sm flex items-center gap-2">
    <!-- ícone x --> Ocorreu um erro. Verifique os dados.
</div>
<!-- Aviso -->
<div class="bg-amber-500/10 border border-amber-500/30 text-amber-400
            px-4 py-3 rounded-lg text-sm">
    Atenção!
</div>
```

### 9.12 Badges de Tipo

```html
<!-- Receita -->
<span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium
             bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
    Receita
</span>
<!-- Despesa -->
<span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium
             bg-rose-500/10 text-rose-400 border border-rose-500/20">
    Despesa
</span>
```

---

## 10. User Stories

### Épico 1: Autenticação e Acesso

---

**US-001 — Registro de Conta**

> _Como_ visitante do sistema,
> _Quero_ criar uma conta com meu nome, e-mail e senha,
> _Para_ ter acesso ao sistema de gestão financeira.

**Critérios de Aceite:**
- [ ] Formulário de registro solicita: primeiro nome, sobrenome, e-mail e senha.
- [ ] E-mail deve ser único no sistema; exibir erro se já cadastrado.
- [ ] Senha deve ter no mínimo 8 caracteres.
- [ ] Após registro bem-sucedido, usuário é autenticado e redirecionado ao dashboard.
- [ ] Perfil é criado automaticamente via signal.

---

**US-002 — Login com E-mail**

> _Como_ usuário cadastrado,
> _Quero_ fazer login com meu e-mail e senha,
> _Para_ acessar meu painel financeiro.

**Critérios de Aceite:**
- [ ] Campo de login aceita e-mail (não username).
- [ ] Exibir mensagem de erro genérica para credenciais inválidas (não indicar qual campo está errado).
- [ ] Após login bem-sucedido, redirecionar para dashboard.
- [ ] Manter usuário logado via session (comportamento padrão Django).

---

**US-003 — Logout**

> _Como_ usuário autenticado,
> _Quero_ encerrar minha sessão,
> _Para_ proteger minha conta em dispositivos compartilhados.

**Critérios de Aceite:**
- [ ] Opção de logout disponível na sidebar.
- [ ] Após logout, redirecionar para landing page.
- [ ] Sessão é invalidada corretamente.

---

### Épico 2: Contas Bancárias

---

**US-010 — Criar Conta Bancária**

> _Como_ usuário autenticado,
> _Quero_ cadastrar minhas contas bancárias,
> _Para_ organizar minhas finanças por conta.

**Critérios de Aceite:**
- [ ] Formulário com: nome da conta, tipo (Corrente/Poupança/Carteira/Investimento), saldo inicial.
- [ ] Conta é criada vinculada ao usuário logado.
- [ ] Saldo inicial é registrado como saldo atual da conta.
- [ ] Exibir mensagem de sucesso após criação.

---

**US-011 — Listar e Visualizar Contas**

> _Como_ usuário autenticado,
> _Quero_ ver todas as minhas contas com seus saldos,
> _Para_ ter visibilidade consolidada dos meus recursos.

**Critérios de Aceite:**
- [ ] Listar somente contas do usuário logado.
- [ ] Exibir nome, tipo e saldo atual de cada conta.
- [ ] Exibir saldo total de todas as contas.

---

**US-012 — Editar e Excluir Conta**

> _Como_ usuário autenticado,
> _Quero_ editar ou excluir minhas contas,
> _Para_ manter meu cadastro atualizado.

**Critérios de Aceite:**
- [ ] Editar nome e tipo da conta.
- [ ] Excluir conta somente se não houver transações vinculadas.
- [ ] Exibir mensagem de erro se tentativa de exclusão com transações existentes.
- [ ] Confirmação antes de excluir.

---

### Épico 3: Categorias

---

**US-020 — Gerenciar Categorias**

> _Como_ usuário autenticado,
> _Quero_ criar, editar e excluir categorias personalizadas,
> _Para_ classificar minhas transações de forma personalizada.

**Critérios de Aceite:**
- [ ] Exibir categorias padrão do sistema (somente leitura) e categorias do usuário.
- [ ] Criar categoria com: nome, tipo (receita/despesa) e ícone (emoji ou texto).
- [ ] Editar somente categorias do próprio usuário.
- [ ] Excluir somente categorias sem transações vinculadas.

---

### Épico 4: Transações

---

**US-030 — Registrar Transação**

> _Como_ usuário autenticado,
> _Quero_ registrar receitas e despesas,
> _Para_ manter meu histórico financeiro atualizado.

**Critérios de Aceite:**
- [ ] Formulário com: tipo (receita/despesa), descrição, valor, data, conta, categoria.
- [ ] Valor deve ser positivo e maior que zero.
- [ ] Ao salvar, atualizar saldo da conta correspondente.
- [ ] Somente contas e categorias do próprio usuário (ou padrão) são exibidas.

---

**US-031 — Listar e Filtrar Transações**

> _Como_ usuário autenticado,
> _Quero_ ver meu histórico de transações com filtros,
> _Para_ analisar meu fluxo financeiro por período e categoria.

**Critérios de Aceite:**
- [ ] Listar transações do mês atual por padrão.
- [ ] Filtrar por: mês/ano, tipo (receita/despesa), categoria.
- [ ] Exibir total de receitas, despesas e saldo do período filtrado.
- [ ] Somente transações do usuário logado.

---

**US-032 — Editar e Excluir Transação**

> _Como_ usuário autenticado,
> _Quero_ corrigir ou remover transações,
> _Para_ manter meu histórico financeiro correto.

**Critérios de Aceite:**
- [ ] Editar todos os campos da transação.
- [ ] Ao editar valor ou conta, recalcular saldo das contas afetadas.
- [ ] Ao excluir, reverter o impacto no saldo da conta.
- [ ] Confirmação antes de excluir.

---

### Épico 5: Dashboard e Perfil

---

**US-040 — Dashboard Financeiro**

> _Como_ usuário autenticado,
> _Quero_ ver um resumo financeiro ao entrar no sistema,
> _Para_ ter uma visão rápida da minha situação financeira atual.

**Critérios de Aceite:**
- [ ] Cards com: total de receitas do mês, total de despesas do mês, saldo do mês.
- [ ] Lista das 5 últimas transações registradas.
- [ ] Lista de contas com seus saldos atuais.

---

**US-050 — Gerenciar Perfil**

> _Como_ usuário autenticado,
> _Quero_ visualizar e editar meus dados e alterar minha senha,
> _Para_ manter meu cadastro atualizado.

**Critérios de Aceite:**
- [ ] Exibir nome, e-mail do usuário logado.
- [ ] Editar primeiro nome e sobrenome.
- [ ] Alterar senha com validação de senha atual + confirmação.

---

## 11. Métricas de Sucesso

### 11.1 KPIs de Produto

| KPI                              | Meta MVP        | Observação                              |
|----------------------------------|-----------------|-----------------------------------------|
| Funcionalidades entregues        | 100% do escopo  | Todos os RF-Must Have implementados     |
| Cobertura do design system       | 100% das telas  | Nenhuma tela sem o template base        |
| Zero erros 500 em fluxos críticos| 0 erros         | Registro, login, CRUD de transações     |
| Tempo de resposta (listagens)    | < 500ms         | Para bases de até 5.000 registros       |
| Responsividade mobile            | 100% das telas  | Testado em viewport 375px               |

### 11.2 KPIs de Qualidade de Código

| KPI                              | Meta            |
|----------------------------------|-----------------|
| Conformidade PEP 8               | 100%            |
| Uso de CBVs                      | > 90% das views |
| Sem lógica de negócio em templates | 100%          |
| Isolamento de dados por usuário  | 100% das queries|

### 11.3 KPIs de Experiência do Usuário

| KPI                              | Meta            |
|----------------------------------|-----------------|
| Fluxo de registro completo       | ≤ 3 cliques     |
| Registro de nova transação       | ≤ 4 campos obrigatórios |
| Feedback visual em todas as ações| 100% (mensagens Django Messages) |
| Interface em português correto   | 100%            |

---

## 12. Riscos e Mitigações

| Risco                                                    | Probabilidade | Impacto   | Mitigação                                                                      |
|----------------------------------------------------------|---------------|-----------|--------------------------------------------------------------------------------|
| Não usar `CustomUser` desde o início                     | Alta          | Crítico   | ⚠️ Configurar `AUTH_USER_MODEL` ANTES da primeira migration                    |
| `SECRET_KEY` exposta no `settings.py`                    | Alta (já ocorreu) | Alto  | Mover para `.env` via `python-decouple` ou variável de ambiente                |
| Saldo de conta fora de sincronia com transações          | Média         | Alto      | Recalcular saldo via method no model ou signal; nunca armazenar saldo sem transação |
| TailwindCSS via CDN pode ter classes purged em produção  | Baixa (CDN não purga) | Médio | Usar CDN Play no desenvolvimento; configurar build para produção na Sprint 5  |
| Queries N+1 na listagem de transações                    | Média         | Médio     | Usar `select_related('account', 'category')` nas views                        |
| Acesso cruzado de dados entre usuários                   | Baixa         | Crítico   | Sempre filtrar por `user=request.user` em TODAS as queries                    |
| Escopo crescente (feature creep)                         | Alta          | Médio     | Seguir PRD rigorosamente; nada além do documentado no MVP                     |
| SQLite com múltiplos acessos simultâneos em produção     | Média         | Alto      | Aviso explícito: SQLite é para desenvolvimento; PostgreSQL na Sprint 5         |

---

## 13. Lista de Tarefas (Sprints)

---

### 🏁 Sprint 0 — Setup e Fundação do Projeto

**Objetivo:** Preparar o ambiente, configurações globais e estrutura base do projeto.

---

- [ ] **0.1 — Configuração do Ambiente Python**
  - [ ] 0.1.1 — Criar e ativar virtualenv (`python -m venv .venv`)
  - [ ] 0.1.2 — Instalar Django 6.x (`pip install django`)
  - [ ] 0.1.3 — Gerar `requirements.txt` (`pip freeze > requirements.txt`)
  - [ ] 0.1.4 — Criar arquivo `.gitignore` com: `.venv/`, `db.sqlite3`, `*.pyc`, `__pycache__/`, `.env`
  - [ ] 0.1.5 — Criar arquivo `.env` para variáveis sensíveis e adicionar ao `.gitignore`

- [ ] **0.2 — Configuração do `settings.py`**
  - [ ] 0.2.1 — Mover `SECRET_KEY` para variável de ambiente (usando `os.environ.get` ou `python-decouple`)
  - [ ] 0.2.2 — Configurar `AUTH_USER_MODEL = 'users.CustomUser'` (antes de qualquer migration)
  - [ ] 0.2.3 — Adicionar todos os apps ao `INSTALLED_APPS`: `accounts`, `categories`, `profiles`, `transactions`, `users`
  - [ ] 0.2.4 — Configurar `LANGUAGE_CODE = 'pt-br'` e `TIME_ZONE = 'America/Sao_Paulo'`
  - [ ] 0.2.5 — Configurar diretório de templates globais: `TEMPLATES[0]['DIRS'] = [BASE_DIR / 'templates']`
  - [ ] 0.2.6 — Configurar `STATIC_URL` e `STATICFILES_DIRS`
  - [ ] 0.2.7 — Configurar `LOGIN_URL`, `LOGIN_REDIRECT_URL` e `LOGOUT_REDIRECT_URL`

- [ ] **0.3 — Configuração de URLs raiz (`core/urls.py`)**
  - [ ] 0.3.1 — Incluir `path('', include('users.urls'))` para landing e autenticação
  - [ ] 0.3.2 — Incluir `path('accounts/', include('accounts.urls'))`
  - [ ] 0.3.3 — Incluir `path('categories/', include('categories.urls'))`
  - [ ] 0.3.4 — Incluir `path('transactions/', include('transactions.urls'))`
  - [ ] 0.3.5 — Incluir `path('profile/', include('profiles.urls'))`
  - [ ] 0.3.6 — Incluir `path('dashboard/', include('core_views'))` ou criar view de dashboard em app dedicada

- [ ] **0.4 — Template Base Global (`templates/base.html`)**
  - [ ] 0.4.1 — Criar arquivo `templates/base.html` com estrutura HTML5 completa
  - [ ] 0.4.2 — Incluir link da fonte Inter do Google Fonts
  - [ ] 0.4.3 — Incluir CDN do TailwindCSS Play (`<script src="https://cdn.tailwindcss.com"></script>`)
  - [ ] 0.4.4 — Definir bloco `{% block title %}` para título dinâmico por página
  - [ ] 0.4.5 — Definir bloco `{% block content %}` para conteúdo de cada página
  - [ ] 0.4.6 — Implementar renderização de mensagens Django Messages com estilo do design system
  - [ ] 0.4.7 — Criar `templates/base_auth.html` (layout com sidebar) herdando de `base.html`
  - [ ] 0.4.8 — Implementar sidebar com: logo Finanpy, links de navegação, dados do usuário logado e botão de logout
  - [ ] 0.4.9 — Implementar destaque de item ativo na sidebar usando `request.resolver_match.url_name`

---

### 🚀 Sprint 1 — App `users`: Autenticação e Usuário Customizado

**Objetivo:** Implementar modelo de usuário com login por e-mail e fluxos de autenticação.

---

- [ ] **1.1 — Model `CustomUser` (`users/models.py`)**
  - [ ] 1.1.1 — Criar classe `CustomUser` herdando de `AbstractUser`
  - [ ] 1.1.2 — Adicionar campo `email = models.EmailField(unique=True)` (sem aspas duplas)
  - [ ] 1.1.3 — Adicionar campos `created_at = models.DateTimeField(auto_now_add=True)` e `updated_at = models.DateTimeField(auto_now=True)`
  - [ ] 1.1.4 — Definir `USERNAME_FIELD = 'email'`
  - [ ] 1.1.5 — Definir `REQUIRED_FIELDS = ['first_name', 'last_name']` (remove username dos required)
  - [ ] 1.1.6 — Adicionar campo `username` como opcional/nulo ou removê-lo (definir estratégia)
  - [ ] 1.1.7 — Registrar no `admin.py` com `UserAdmin` customizado

- [ ] **1.2 — Backend de Autenticação por E-mail (`users/backends.py`)**
  - [ ] 1.2.1 — Criar classe `EmailBackend` herdando de `ModelBackend`
  - [ ] 1.2.2 — Sobrescrever método `authenticate(request, email=None, password=None, **kwargs)`
  - [ ] 1.2.3 — Buscar usuário por `email` ao invés de `username`
  - [ ] 1.2.4 — Adicionar `AUTHENTICATION_BACKENDS = ['users.backends.EmailBackend']` no `settings.py`

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

---

*PRD gerado por análise arquitetural em 2026-07-15 · Finanpy v1.0.0*
