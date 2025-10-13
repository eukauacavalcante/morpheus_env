# Ferramentas e Dependências

Descrição detalhada das ferramentas, bibliotecas e dependências utilizadas no Morpheus Env.

---

## Backend

### Django 5.2.6

Framework web Python. Uso no projeto:

- MVT (Model-View-Template) architecture
- ORM para banco de dados
- Admin panel customizável
- Autenticação integrada
- Proteção CSRF e XSS
- Middleware de segurança

```bash
pip install Django==5.2.6
```

---

### psutil 7.0.0

Coleta métricas de sistema (CPU, RAM, disco).

**Uso**: `tools/services/system_metrics.py`

```python
import psutil

cpu_percent = psutil.cpu_percent(interval=1)
ram = psutil.virtual_memory()
disk = psutil.disk_usage('/')
```

**Na prática**:

```python
# tools/services/system_metrics.py
def get_system_status():
    return {
        'cpu_percent': psutil.cpu_percent(),
        'ram_percent': psutil.virtual_memory().percent,
        'memory_used': disk.used / (1024**3),
    }
```

```bash
pip install psutil==7.0.0
```

---

### Groq 0.31.1

SDK Python para IA Groq. Análise inteligente de métricas.

**Uso**: `tools/services/ai_analysis.py`

```python
from groq import Groq

client = Groq(api_key='sua-api-key')
response = client.chat.completions.create(
    model='mixtral-8x7b-32768',
    messages=[
        {'role': 'system', 'content': 'Você é um assistente...'},
        {'role': 'user', 'content': 'Analise estes dados...'}
    ]
)
```

**Na prática**:

Sistema envia métricas (CPU, RAM em níveis "high"/"normal") e recebe análise em texto.

```bash
pip install groq==0.31.1
```

---

### google-auth 2.41.1

Autenticação OAuth2 para Gmail. Envio de emails seguro.

**Uso**: `notifications/utils/email_oauth2.py`

```python
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

creds = Credentials(
    None,
    refresh_token=refresh_token,
    token_uri='https://oauth2.googleapis.com/token',
    client_id=client_id,
    client_secret=client_secret
)
creds.refresh(Request())
```

**Na prática**: Renovação automática de access token para envio de emails.

```bash
pip install google-auth==2.41.1
```

---

### python-decouple 3.8

Gerenciador de variáveis de ambiente (.env).

**Uso**: `core/settings.py`

```python
from decouple import config

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', 'False') == 'True'
TIMEOUT = config('TIMEOUT', cast=int, default=30)
```

**Na prática**: Carrega variáveis sensíveis sem hardcode.

```bash
pip install python-decouple==3.8
```

---

### colorama 0.4.6

Cores no terminal. Mensagens de notificação coloridas.

**Uso**: `notifications/utils/colors.py`

```python
from colorama import Fore, Style

print(Fore.GREEN + "Sucesso!")
print(Fore.RED + "Erro!")
print(Fore.YELLOW + "Aviso")
```

**Na prática**: Feedback visual em logs e notificações.

```bash
pip install colorama==0.4.6
```

---

### django-ratelimit 4.1.0

Rate limiting para APIs. Proteção contra abuso.

**Uso**: `tools/views.py`

```python
from django_ratelimit.decorators import ratelimit

@method_decorator(
    ratelimit(key='user', rate='20/m', method='GET'),
    name='dispatch'
)
class SystemAnalysisAPIView(LoginRequiredMixin, generic.View):
    pass
```

**Na prática**: Máximo 20 requisições/minuto por usuário para métricas.

```bash
pip install django-ratelimit==4.1.0
```

---

## Frontend

### Tailwind CSS 4

Framework CSS utility-first para estilização.

**Uso**: `static/css/styles.css` (compilado)

```html
<div class="bg-purple-500 text-white p-4 rounded-lg">
    <h1 class="text-2xl font-bold">Título</h1>
</div>
```

**Compilação**:

```bash
bash build-tailwind.sh
```

**Configuração**: `tailwind.config.js`

```javascript
module.exports = {
  content: [
    './core/templates/**/*.html',
    './tools/templates/**/*.html',
    './users/templates/**/*.html',
  ],
}
```

---

### Bootstrap Icons 1.13.1

Conjunto de ícones SVG.

**Uso**: `core/templates/base.html`

```html
<link rel="stylesheet" 
      href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.13.1/font/bootstrap-icons.min.css">

<!-- Usar -->
<i class="bi bi-github"></i>
<i class="bi bi-briefcase-fill"></i>
```

**Ícones disponíveis**: [icons.getbootstrap.com](https://icons.getbootstrap.com)

---

## Desenvolvimento

### flake8 7.3.0

Linter Python para qualidade de código (PEP 8).

```bash
flake8 .
flake8 tools/views.py
```

```bash
pip install flake8==7.3.0
```

---

### isort 6.1.0

Ordena imports Python automaticamente.

```bash
isort .
isort . --check-only
```

```bash
pip install isort==6.1.0
```

---

## Instalação

```bash
# Todos os requisitos
pip install -r requirements.txt

# Desenvolvimento
pip install -r requirements_dev.txt

# Individual
pip install Django psutil groq google-auth python-decouple colorama django-ratelimit
```

---

## Produção (Opcional)

### gunicorn

Servidor WSGI HTTP para produção.

```bash
pip install gunicorn
gunicorn core.wsgi:application --workers=4
```

---

### psycopg2-binary

Driver PostgreSQL para Python.

```bash
pip install psycopg2-binary
```

**Configuração** (`settings.py`):

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'morpheus_db',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

---

### django-redis

Cache backend Redis para Django.

```bash
pip install django-redis
```

**Configuração**:

```python
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
    }
}
```

---

### whitenoise

Servidor de arquivos estáticos para produção.

```bash
pip install whitenoise
```

**Configuração** (`settings.py`):

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # ... resto
]
```

---

## Próximas Etapas

- [Instalação](./installation.md) - Como instalar
- [Configuração](./configuration.md) - Variáveis de ambiente
