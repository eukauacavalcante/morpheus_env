# Instalação e Setup

Guia passo a passo para clonar, configurar e executar o Morpheus Env localmente.

---

## Instalação Básica

### 1. Clonar Repositório

```bash
git clone https://github.com/eukauacavalcante/morpheus_env.git
cd morpheus_env
```

### 2. Criar Ambiente Virtual

```bash
# Linux/macOS
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar .env

```bash
cp .env.example .env
```

Edite `.env`:

```env
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
EMAIL_MODE=False
AI_MODE=False
SECRET_KEY=seu-django-secret-key-aqui
```

Gerar `SECRET_KEY`:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 5. Banco de Dados

```bash
python manage.py migrate
python manage.py createsuperuser
```

### 6. Servidor

```bash
python manage.py runserver
```

Acesse: `http://localhost:8000`

---

## Configuração Opcional

### Ativar Email (Gmail + OAuth2)

1. **Criar App Password**:

   - Acesse [myaccount.google.com/security](https://myaccount.google.com/security)
   - Ative autenticação de 2 fatores
   - Em "Senhas de app", gere uma nova senha (16 caracteres)

2. **Configurar .env**:

```env
EMAIL_MODE=True
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=seu-email@gmail.com
EMAIL_HOST_PASSWORD=senha-de-app-16-caracteres
DEFAULT_FROM_EMAIL=seu-email@gmail.com
```

3. **Testar**:

```bash
python manage.py shell
```

Dentro do shell:

```python
from django.core.mail import send_mail
send_mail(
    'Teste',
    'Mensagem de teste',
    'seu-email@gmail.com',
    ['seu-email@gmail.com'],
    fail_silently=False,
)
```

---

### Ativar IA (Groq)

1. **Criar conta Groq**:

   - Acesse [console.groq.com](https://console.groq.com)
   - Crie conta gratuita
   - Gere API key

2. **Configurar .env**:

```env
AI_MODE=True
API_KEY=sua-api-key-groq
AI_MODEL=mixtral-8x7b-32768
```

3. **Testar**:

```bash
python manage.py shell
```

Dentro do shell:

```python
from tools.services.ai_analysis import get_ai_analysis
analysis = get_ai_analysis()
print(analysis)
```

---

### Configurar OAuth2 Google (Avançado)

Para envio de emails mais seguro via OAuth2 (não recomendado para produção sem HTTPS).

1. **Criar projeto Google Cloud**:

   - Acesse [console.cloud.google.com](https://console.cloud.google.com)
   - Crie novo projeto
   - Ative "Gmail API"

2. **Criar credenciais OAuth2**:

   - Tipo: "Desktop application"
   - Download JSON das credenciais

3. **Gerar Refresh Token**:

```python
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/gmail.send']
flow = InstalledAppFlow.from_client_secrets_file(
    'sua-credenciais.json',
    SCOPES
)
creds = flow.run_local_server(port=0)
print('Refresh Token:', creds.refresh_token)
```

4. **Configurar .env**:

```env
GOOGLE_OAUTH2_CLIENT_ID=seu-client-id
GOOGLE_OAUTH2_CLIENT_SECRET=seu-client-secret
GOOGLE_OAUTH2_REFRESH_TOKEN=seu-refresh-token
EMAIL_MODE=True
```

---

## Compilar Tailwind CSS

Se modificar `static/css/input.css`:

```bash
bash build-tailwind.sh
```

---

## Possíveis Erros

### Erro: "No module named 'django'"

```bash
# Verificar se venv está ativado
which python  # Deve mostrar venv/bin/python

# Reinstalar
pip install -r requirements.txt
```

### Erro: "Port 8000 already in use"

```bash
# Usar porta diferente
python manage.py runserver 8001
```

### Erro: "Database is locked"

```bash
# Deletar e recriar
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

---

## Próximas Etapas

- [Desenvolvimento](./development.md) - Workflow de desenvolvimento
- [Configuração](./configuration.md) - Variáveis de ambiente
