# Finanpy — Agentes de IA

Agentes especializados para o time de desenvolvimento do projeto Finanpy.
Cada agente conhece a stack, as convenções e os limites do projeto.

---

## Agentes disponíveis

| Agente | Arquivo | Quando usar |
|---|---|---|
| 🔧 Django Backend Developer | [backend.md](./backend.md) | Models, views, forms, URLs, signals, admin, migrations, settings |
| 🎨 Frontend Developer | [frontend.md](./frontend.md) | Templates HTML, TailwindCSS, componentes visuais, design system |
| 🧪 QA / Tester | [qa.md](./qa.md) | Verificar fluxos do sistema, comportamento visual e bugs |

---

## Quando usar cada agente

### 🔧 Backend — `backend.md`

Use quando precisar de:

- Criar ou editar um **model** Django
- Criar ou editar uma **view** (sempre CBV)
- Criar ou editar um **form** (`ModelForm`)
- Criar ou editar **URLs** de uma app
- Criar ou editar **signals**
- Configurar o **admin** de um model
- Rodar ou criar **migrations**
- Ajustar `core/settings.py`
- Implementar o backend de autenticação por e-mail
- Qualquer lógica de negócio em Python

> Usa **MCP context7** para consultar documentação Django atualizada.

---

### 🎨 Frontend — `frontend.md`

Use quando precisar de:

- Criar ou editar um **template HTML**
- Aplicar ou corrigir **classes TailwindCSS**
- Criar o layout de uma **nova tela**
- Implementar o **template base** (`base.html`, `base_auth.html`)
- Construir a **sidebar** de navegação
- Estilizar **formulários**, **tabelas**, **cards** ou **badges**
- Renderizar **mensagens Django** no template
- Garantir **responsividade** em uma tela
- Qualquer ajuste visual ou de componente

> Usa **MCP context7** para consultar documentação DTL e TailwindCSS atualizadas.

---

### 🧪 QA — `qa.md`

Use quando precisar de:

- Verificar se um **fluxo** está funcionando corretamente
- Confirmar se o **design** de uma tela está dentro do esperado
- Testar **autenticação** (registro, login, logout, proteção de rotas)
- Testar **CRUD** de contas, categorias, transações ou perfil
- Verificar **isolamento de dados** entre usuários diferentes
- Checar **responsividade** em diferentes viewports
- Reportar um **bug** com contexto completo

> Usa **MCP Playwright** para navegar e interagir com o sistema rodando localmente.

---

## Fluxo de trabalho sugerido

```
1. Backend implementa a lógica (model + view + form + URL)
2. Frontend cria o template da tela correspondente
3. QA verifica o fluxo completo no browser
4. QA reporta bugs → Backend ou Frontend corrige → QA re-verifica
```

---

## Referências do projeto

| Documento | Conteúdo |
|---|---|
| [`CLAUDE.md`](../CLAUDE.md) | Contexto geral, regras e comandos do projeto |
| [`prd.md`](../prd.md) | Product Requirements Document — escopo completo |
| [`docs/setup.md`](../docs/setup.md) | Como instalar e rodar o projeto |
| [`docs/architecture.md`](../docs/architecture.md) | Estrutura de apps e roteamento |
| [`docs/conventions.md`](../docs/conventions.md) | Padrões de código (PEP 8, aspas simples, CBVs) |
| [`docs/design-system.md`](../docs/design-system.md) | Paleta, tipografia e componentes TailwindCSS |
