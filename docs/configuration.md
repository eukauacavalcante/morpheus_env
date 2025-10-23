# Configuração do Projeto

Este documento descreve todas as variáveis de ambiente e configurações disponíveis no Morpheus Env.

---

## Arquivo .env

Todas as variáveis sensíveis estão em `.env` (não versionado no Git).

**Criar arquivo**:

```bash
cp .env.example .env
```

**⚠️ Nunca commitar .env com valores reais**

---

## Variáveis Obrigatórias

### `SECRET_KEY` (string)

Chave para criptografia de sessão Django.

**Gerar chave segura**:

```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

Copie a saída para `.env`:

```env
SECRET_KEY=django-insecure-abc123xyz789...
```

**⚠️ Mude em produção!**

---

## Variáveis de Django

### `DEBUG` (True/False, padrão: False)

Ativa modo debug. Mostra erros detalhados.

```env
DEBUG=True   # Desenvolvimento
DEBUG=False  # Produção
```

⚠️ **Nunca True em produção!**

### `ALLOWED_HOSTS` (lista, padrão: vazio)

Domínios permitidos de acesso.

```env
# Desenvolvimento
ALLOWED_HOSTS=localhost,127.0.0.1

# Produção
ALLOWED_HOSTS=example.com,www.example.com
```

---

## Variáveis de Email

### `EMAIL_MODE` (True/False, padrão: False)

Ativa ou desativa envio de emails.

```env
EMAIL_MODE=False  # Dev (sem envio)
EMAIL_MODE=True   # Prod (com OAuth2)
```

### `EMAIL_HOST` (padrão: smtp.gmail.com)

Servidor SMTP.

```env
EMAIL_HOST=smtp.gmail.com
```

### `EMAIL_PORT` (padrão: 587)

Porta SMTP (587 para TLS, 465 para SSL).

```env
EMAIL_PORT=587
```

### `EMAIL_USE_TLS` (padrão: True)

```env
EMAIL_USE_TLS=True
```

### `EMAIL_HOST_USER` (necessário se EMAIL_MODE=True)

Email do remetente.

```env
EMAIL_HOST_USER=seu-email@gmail.com
```

### `EMAIL_HOST_PASSWORD` (necessário se EMAIL_MODE=True)

Senha de app do Gmail (não a senha da conta).

```env
EMAIL_HOST_PASSWORD=abc123xyz789abc123xyz
```

Como gerar: Settings → Segurança → Senhas de app (Gmail)

### `DEFAULT_FROM_EMAIL` (necessário se EMAIL_MODE=True)

Email padrão para notificações.

```env
DEFAULT_FROM_EMAIL=seu-email@gmail.com
```

---

## Variáveis de IA (Groq)

### `AI_MODE` (True/False, padrão: False)

Ativa ou desativa análise por IA.

```env
AI_MODE=False  # Dev (sem IA)
AI_MODE=True   # Prod (com Groq)
```

### `API_KEY` (necessário se AI_MODE=True)

Chave de API do Groq. Gere em [console.groq.com](https://console.groq.com)

```env
API_KEY=gsk_abc123xyz789abc123xyz789...
```

### `AI_MODEL` (padrão: mixtral-8x7b-32768)

Modelo de IA do Groq.

```env
AI_MODEL=mixtral-8x7b-32768
```

Opções:
- `mixtral-8x7b-32768` - Rápido e eficiente (recomendado)
- `llama2-70b-4096` - Maior contexto
- `gemma-7b-it` - Leve

---

## Variáveis de OAuth2 Google

Para envio de emails com OAuth2 (mais seguro que senha de app).

### `GOOGLE_OAUTH2_CLIENT_ID`

Client ID do projeto Google Cloud.

```env
GOOGLE_OAUTH2_CLIENT_ID=123456789-abc123xyz789.apps.googleusercontent.com
```

### `GOOGLE_OAUTH2_CLIENT_SECRET`

Client Secret do projeto Google Cloud.

```env
GOOGLE_OAUTH2_CLIENT_SECRET=GOCSPX-abc123xyz789abc123xyz789
```

### `GOOGLE_OAUTH2_REFRESH_TOKEN`

Refresh Token para renovar access token automaticamente.

```env
GOOGLE_OAUTH2_REFRESH_TOKEN=1//abc123xyz789abc123xyz789abc123xyz789
```

Como gerar: Consulte [installation.md](./installation.md) na seção "Configuração de OAuth2 Google (Avançado)"

---

## Configuração por Ambiente

### Desenvolvimento

```env
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
EMAIL_MODE=False
AI_MODE=False
SECRET_KEY=dev-key-insecura
```

### Produção

```env
DEBUG=False
ALLOWED_HOSTS=example.com,www.example.com
EMAIL_MODE=True
AI_MODE=True
SECRET_KEY=super-secreto-muito-seguro
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
```

---

## Variáveis de Banco de Dados

### SQLite (Desenvolvimento)

Padrão. Arquivo `db.sqlite3` é criado automaticamente.

Nenhuma variável necessária.

### PostgreSQL (Produção - Recomendado)

Para usar PostgreSQL em produção, instale:

```bash
pip install psycopg2-binary
```

Configure em `core/settings.py` (não em `.env`):

```python
import dj_database_url

DATABASES = {
    'default': dj_database_url.config(
        default='postgresql://user:pass@localhost:5432/morpheus'
    )
}
```

---

## Rate Limiting

Configurado em `tools/views.py`:

| Endpoint | Limite | Janela |
|----------|--------|--------|
| `/sistema/monitoramento/api/v1/metrics` | 20 | 1 minuto |
| `/sistema/monitoramento/api/v1/ai` | 10 | 1 minuto |
| `/sistema/conversor/api/v1/converter` | Ilimitado | - |

Para alterar, edite o decorator `@method_decorator(ratelimit(...))` nas views.

---

## Tailwind CSS

Arquivo: `tailwind.config.js`

Escaneia templates e JS para classes Tailwind:

```javascript
module.exports = {
  content: [
    './core/templates/**/*.html',
    './tools/templates/**/*.html',
    './users/templates/**/*.html',
  ],
  theme: {
    extend: {},
  },
}
```

Recompile após mudanças CSS:

```bash
bash build-tailwind.sh
```

---

## Próximas Etapas

- [Instalação](./installation.md) - Como configurar tudo
- [Ferramentas](./tools.md) - Dependências do projeto
