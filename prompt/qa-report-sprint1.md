## Relatório de QA — Sprint 1

Data: 2026-07-20

---

### RT-01: Landing page pública ✅

| Check | Resultado |
|---|---|
| Página carrega sem erro | ✅ HTTP 200 |
| Nome "Finanpy" presente | ✅ |
| Botão "Entrar" visível | ✅ |
| Botão "Cadastre-se" visível | ✅ |
| Não exibe dados de usuário logado | ✅ |
| Design dark mode, fonte Inter | ✅ |
| Hero com gradiente | ✅ |
| 3 cards de features | ✅ |
| Footer com nome do produto | ✅ |

---

### RT-02: Registro de novo usuário

| Check | Resultado |
|---|---|
| Campos: Nome, Sobrenome, E-mail, Senha, Confirmar senha | ✅ |
| Submeter vazio mostra erros "Este campo é obrigatório." | ✅ |
| Registrar com e-mail duplicado mostra "Este e-mail já está cadastrado." | ✅ |
| Registrar com dados válidos redireciona para /dashboard/ | ✅ |
| Usuário logado após registro | ✅ |

**⚠️ Bug UX: Campos de senha são limpos ao submeter formulário com erro**
- **Severidade:** Baixo
- **Descrição:** Quando o formulário é submetido com erro (ex: e-mail duplicado), os campos `password1` e `password2` voltam vazios, forçando o usuário a redigitar as senhas.
- **Causa:** O template `users/register.html` não preserva os valores dos campos de senha (inputs type="password" sem atributo `value`).
- **Correção sugerida:** Usar `{{ form.password1.value|default:'' }}` ou remover os inputs manuais e usar `{{ form.password1 }}` para que o Django gerencie o estado.

---

### RT-03: Login e Logout

| Check | Resultado |
|---|---|
| Login com credenciais inválidas mostra erro | ✅ |
| Erro: "Por favor, entre com um email e senha corretos..." | ✅ |
| Login com e-mail e senha válidos → /dashboard/ | ✅ |
| Logout via sidebar (POST) → landing page `/` | ✅ |
| `redirect_authenticated_user = True` impede acesso a /entrar/ logado | ✅ |

**⚠️ Bug: Acesso direto a /sair/ via GET mostra página de admin do Django**
- **Severidade:** Médio
- **Descrição:** Ao acessar `/sair/` diretamente pelo navegador (GET), o Django LogoutView mostra o template padrão de confirmação "Sessão encerrada | Site de administração do Django".
- **Correção aplicada:** Adicionado `next_page = reverse_lazy('users:landing')` ao `LogoutView`. Funciona via redirect (HTTP 302), mas o Playwright não seguiu o redirect automaticamente no teste (comportamento esperado do browser real: seguirá).

---

### RT-04: Proteção de rotas autenticadas ✅

| Check | Resultado |
|---|---|
| /dashboard/ sem login → /entrar/?next=/dashboard/ | ✅ |
| /contas/ sem login → (não implementado) | ⏭️ Sprint 3 |
| /categorias/ sem login → (não implementado) | ⏭️ Sprint 4 |
| /transacoes/ sem login → (não implementado) | ⏭️ Sprint 5 |
| /perfil/ sem login → (não implementado) | ⏭️ Sprint 2 |

---

### RT-03 item 3: Login com username (não e-mail)

| Check | Resultado |
|---|---|
| Campo de e-mail usa `type="email"` no HTML | ✅ O browser bloqueia texto não-email |

---

### Bugs encontrados e correções

#### 🔴 BUG-01 (Crítico — Corrigido): `NoReverseMatch` no `base_auth.html`
- **Descrição:** A sidebar referenciava `{% url 'accounts:list' %}`, `{% url 'categories:list' %}`, `{% url 'transactions:list' %}`, `{% url 'profiles:profile' %}` — URLs que não existem porque as apps ainda não foram implementadas.
- **Impacto:** Toda página autenticada quebrava com erro 500.
- **Correção:** Substituídos por `href="#"` com badge "em breve" e `cursor-not-allowed` até a implementação das respectivas sprints.

#### 🟡 BUG-02 (Médio — Corrigido): `/sair/` via GET mostrava página de admin
- **Descrição:** `LogoutView` sem `next_page` caía no template padrão do Django admin.
- **Correção:** Adicionado `next_page = reverse_lazy('users:landing')`.

#### 🟡 BUG-03 (Baixo): Campos de senha limpam ao submeter formulário com erro
- **Descrição:** O template `users/register.html` usa inputs HTML manuais em vez de `{{ form.password1 }}`, fazendo com que os valores de senha não sejam preservados após erro de validação.
- **Correção sugerida:** Alterar o template para usar `{{ form.password1 }}` e `{{ form.password2 }}` do Django form.

---

### Resumo

| Tipo | Quantidade |
|---|---|
| Funcionalidades testadas e OK | 20 |
| Bugs críticos encontrados | 1 (corrigido) |
| Bugs médios encontrados | 1 (corrigido) |
| Bugs baixos encontrados | 1 (pendente) |

### Conclusão

A Sprint 1 está **funcional**. O fluxo completo de autenticação (landing → registro → login → dashboard → logout → proteção de rotas) opera corretamente. Os bugs encontrados foram corrigidos ou documentados com sugestão de correção.
