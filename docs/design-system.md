# Design System — Padrões Visuais

O Finanpy usa **TailwindCSS** (via CDN) dentro do **Django Template Language**.
O design é dark mode com gradientes vibrantes e componentes consistentes em
todas as telas.

> **Regra:** Toda tela deve herdar do template base. Nenhum componente deve
> fugir das classes documentadas aqui.

---

## Fonte

Fonte [Inter](https://fonts.google.com/specimen/Inter) do Google Fonts,
incluída no `<head>` do template base.

```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
```

Aplicada no `<body>`:

```html
<body class="font-['Inter'] bg-gray-950 text-white antialiased">
```

---

## Paleta de cores

| Papel | Classe TailwindCSS | Hex | Uso |
|---|---|---|---|
| Fundo principal | `bg-gray-950` | `#030712` | Fundo global |
| Fundo card | `bg-gray-900` | `#111827` | Cards, formulários |
| Fundo elevado | `bg-gray-800` | `#1f2937` | Inputs, hover |
| Borda | `border-gray-800` / `border-gray-700` | — | Bordas gerais |
| Primária | `from-violet-600 to-indigo-600` | gradiente | Botão primário, destaques |
| Primária hover | `from-violet-500 to-indigo-500` | gradiente | Estado hover do primário |
| Receita | `text-emerald-400` | `#34d399` | Valores positivos |
| Despesa | `text-rose-400` | `#fb7185` | Valores negativos |
| Texto principal | `text-white` | `#ffffff` | Títulos, valores |
| Texto secundário | `text-gray-300` | `#d1d5db` | Textos de apoio |
| Label | `text-gray-400` | `#9ca3af` | Labels de formulário |
| Accent | `text-violet-400` | `#a78bfa` | Links, ícones |

---

## Tipografia

| Elemento | Classes |
|---|---|
| Título da página (H1) | `text-3xl font-bold text-white` |
| Título de seção (H2) | `text-xl font-semibold text-white` |
| Título de card (H3) | `text-lg font-medium text-gray-100` |
| Texto de corpo | `text-sm text-gray-300` |
| Label de formulário | `text-sm font-medium text-gray-400` |
| Valor monetário | `text-2xl font-bold tabular-nums` |
| Badge / tag | `text-xs font-medium` |

---

## Logo

```html
<span class="bg-gradient-to-r from-violet-400 to-indigo-400 bg-clip-text text-transparent font-bold text-xl">
    Finanpy
</span>
```

---

## Botões

### Primário
Ação principal da tela (salvar, criar, confirmar).

```html
<button class="bg-gradient-to-r from-violet-600 to-indigo-600
               hover:from-violet-500 hover:to-indigo-500
               text-white font-semibold py-2.5 px-6 rounded-lg
               transition-all duration-200
               focus:outline-none focus:ring-2 focus:ring-violet-500 focus:ring-offset-2 focus:ring-offset-gray-900
               disabled:opacity-50 disabled:cursor-not-allowed">
    Salvar
</button>
```

### Secundário
Ação secundária (cancelar, voltar).

```html
<button class="border border-gray-600 hover:border-gray-500
               text-gray-300 hover:text-white
               font-medium py-2.5 px-6 rounded-lg
               transition-all duration-200 hover:bg-gray-800">
    Cancelar
</button>
```

### Perigo
Ação destrutiva (excluir).

```html
<button class="bg-rose-600 hover:bg-rose-500
               text-white font-medium py-2 px-4 rounded-lg
               transition-colors duration-200">
    Excluir
</button>
```

### Ícone
Botão compacto com ícone SVG.

```html
<button class="p-2 rounded-lg text-gray-400 hover:text-white hover:bg-gray-700
               transition-colors duration-200">
    <!-- SVG -->
</button>
```

---

## Inputs e formulários

### Estrutura de campo

```html
<div class="space-y-1">
    <label for="campo" class="block text-sm font-medium text-gray-400">
        Nome do campo
    </label>
    <input
        type="text"
        id="campo"
        name="campo"
        class="w-full bg-gray-800 border border-gray-700
               text-white placeholder-gray-500
               rounded-lg px-4 py-2.5
               focus:outline-none focus:ring-2 focus:ring-violet-500 focus:border-transparent
               transition-all duration-200"
    >
    <!-- erro (se houver) -->
    <p class="text-xs text-rose-400">Mensagem de erro.</p>
</div>
```

### Select

```html
<select class="w-full bg-gray-800 border border-gray-700
               text-white rounded-lg px-4 py-2.5
               focus:outline-none focus:ring-2 focus:ring-violet-500 focus:border-transparent">
    <option>Selecione...</option>
</select>
```

### Textarea

```html
<textarea rows="3"
          class="w-full bg-gray-800 border border-gray-700
                 text-white placeholder-gray-500
                 rounded-lg px-4 py-2.5 resize-none
                 focus:outline-none focus:ring-2 focus:ring-violet-500 focus:border-transparent">
</textarea>
```

---

## Cards

### Card padrão

```html
<div class="bg-gray-900 border border-gray-800 rounded-xl p-6
            hover:border-gray-700 transition-colors duration-200">
    <!-- conteúdo -->
</div>
```

### Card de métrica (dashboard)

```html
<div class="bg-gray-900 border border-gray-800 rounded-xl p-6">
    <div class="flex items-center justify-between mb-2">
        <span class="text-sm text-gray-400">Label da métrica</span>
        <span class="p-2 bg-emerald-500/10 rounded-lg text-emerald-400">
            <!-- ícone SVG -->
        </span>
    </div>
    <p class="text-2xl font-bold text-emerald-400 tabular-nums">R$ 0,00</p>
    <p class="text-xs text-gray-500 mt-1">Mês atual</p>
</div>
```

---

## Tabelas

```html
<div class="overflow-x-auto rounded-xl border border-gray-800">
    <table class="w-full text-sm">
        <thead class="bg-gray-800/50">
            <tr>
                <th class="text-left text-gray-400 font-medium px-6 py-4">Coluna</th>
            </tr>
        </thead>
        <tbody class="divide-y divide-gray-800">
            <tr class="hover:bg-gray-800/30 transition-colors duration-150">
                <td class="px-6 py-4 text-gray-200">Valor</td>
            </tr>
        </tbody>
    </table>
</div>
```

---

## Badges

### Receita

```html
<span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium
             bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
    Receita
</span>
```

### Despesa

```html
<span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium
             bg-rose-500/10 text-rose-400 border border-rose-500/20">
    Despesa
</span>
```

---

## Mensagens (Django Messages)

```html
<!-- Sucesso -->
<div class="bg-emerald-500/10 border border-emerald-500/30 text-emerald-400
            px-4 py-3 rounded-lg text-sm">
    Operação realizada com sucesso.
</div>

<!-- Erro -->
<div class="bg-rose-500/10 border border-rose-500/30 text-rose-400
            px-4 py-3 rounded-lg text-sm">
    Ocorreu um erro. Verifique os dados.
</div>

<!-- Aviso -->
<div class="bg-amber-500/10 border border-amber-500/30 text-amber-400
            px-4 py-3 rounded-lg text-sm">
    Atenção!
</div>
```

---

## Layout das páginas autenticadas

Todas as telas autenticadas usam o layout: **sidebar fixa à esquerda + conteúdo principal à direita**.

```html
<div class="min-h-screen bg-gray-950 flex">

    <!-- Sidebar -->
    <aside class="w-64 bg-gray-900 border-r border-gray-800 flex flex-col min-h-screen">

        <!-- Logo -->
        <div class="px-6 py-5 border-b border-gray-800">
            <span class="bg-gradient-to-r from-violet-400 to-indigo-400
                         bg-clip-text text-transparent font-bold text-xl">
                Finanpy
            </span>
        </div>

        <!-- Navegação -->
        <nav class="flex-1 px-4 py-6 space-y-1">
            <a href="{% url 'dashboard' %}"
               class="flex items-center gap-3 px-4 py-2.5 rounded-lg
                      text-gray-400 hover:text-white hover:bg-gray-800
                      transition-colors duration-200">
                Dashboard
            </a>
        </nav>

        <!-- Usuário logado -->
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

    <!-- Conteúdo principal -->
    <main class="flex-1 overflow-y-auto">
        <div class="p-8 max-w-7xl mx-auto">
            {% block content %}{% endblock %}
        </div>
    </main>

</div>
```

### Item ativo na sidebar

O item de navegação ativo recebe destaque visual:

```html
class="... {% if request.resolver_match.url_name == 'list' %}
    bg-violet-600/20 text-violet-400 border border-violet-600/30
{% endif %}"
```

---

## Grid de cards

```html
<!-- 3 colunas no desktop, 1 no mobile -->
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
    <!-- cards -->
</div>
```

---

## Fundo com gradiente (seções de destaque)

```html
<div class="bg-gradient-to-br from-gray-950 via-gray-900 to-violet-950">
    <!-- conteúdo -->
</div>
```
