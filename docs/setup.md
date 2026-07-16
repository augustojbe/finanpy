# Setup — Configurando o Projeto

## Pré-requisitos

- Python 3.12+
- pip

## Instalação

**1. Clonar o repositório e entrar na pasta do projeto**

```bash
git clone <url-do-repositorio>
cd finanpy
```

**2. Criar e ativar o ambiente virtual**

```bash
python -m venv .venv
source .venv/bin/activate      # Linux / macOS
.venv\Scripts\activate         # Windows
```

**3. Instalar as dependências**

```bash
pip install -r requirements.txt
```

**4. Rodar as migrations**

```bash
python manage.py migrate
```

**5. Criar um superusuário (opcional, para acessar o admin)**

```bash
python manage.py createsuperuser
```

**6. Iniciar o servidor de desenvolvimento**

```bash
python manage.py runserver
```

Acesse em: `http://127.0.0.1:8000`

---

## Dependências atuais

Listadas em [`requirements.txt`](../requirements.txt):

| Pacote | Versão | Função |
|---|---|---|
| Django | 6.0.7 | Framework principal |
| asgiref | 3.12.1 | Suporte ASGI (Django) |
| sqlparse | 0.5.5 | Parser SQL (Django) |

---

## Banco de dados

O projeto usa **SQLite**, o banco padrão do Django. O arquivo `db.sqlite3` é
criado automaticamente na raiz do projeto após a primeira `migrate`.

Não é necessária nenhuma configuração adicional de banco de dados para rodar
localmente.

---

## Variáveis de ambiente

Atualmente o projeto usa as configurações padrão em `core/settings.py`.

> ⚠️ A `SECRET_KEY` presente no `settings.py` é insegura e deve ser movida
> para uma variável de ambiente antes de qualquer deploy em produção.

---

## Django Admin

Disponível em `http://127.0.0.1:8000/admin/` após criar um superusuário.
