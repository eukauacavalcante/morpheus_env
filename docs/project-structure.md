# Estrutura do Projeto

Mapa completo de diretórios e arquivos do Morpheus Env com descrição de cada elemento.

---

## Árvore de Diretórios

```
morpheus_env/
│
├── core/                          # Configurações centrais Django
│   ├── templates/
│   │   ├── base.html              # Template base (herança)
│   │   ├── index.html             # Home
│   │   └── components/
│   │       ├── _header.html
│   │       └── _footer.html
│   ├── settings.py                # Configurações Django
│   ├── urls.py                    # Rotas globais
│   ├── views.py                   # Views globais
│   ├── wsgi.py                    # Configuração WSGI
│   └── asgi.py                    # Configuração ASGI
│
├── users/                         # App autenticação
│   ├── migrations/                # Histórico banco de dados
│   ├── templates/registration/
│   │   ├── login.html
│   │   └── register.html
│   ├── validators/
│   │   └── disposable_email_blocklist.conf  # Emails bloqueados
│   ├── forms.py                   # Formulários customizados
│   ├── models.py                  # Modelos de dados
│   ├── signals.py                 # Sinais (emails automáticos)
│   ├── urls.py                    # Rotas
│   ├── views.py                   # Views
│   └── admin.py                   # Admin panel
│
├── tools/                         # App ferramentas
│   ├── services/                  # Lógica de negócio
│   │   ├── system_metrics.py
│   │   ├── ai_analysis.py
│   │   └── num_converter.py
│   ├── templates/
│   │   ├── system_analysis.html
│   │   └── num_converter.html
│   ├── views.py                   # Views e APIs
│   ├── urls.py                    # Rotas
│   ├── admin.py
│   └── migrations/
│
├── notifications/                 # App notificações
│   ├── utils/
│   │   ├── send_email.py
│   │   ├── email_oauth2.py
│   │   ├── colors.py
│   │   ├── emails.py
│   │   └── terminal_msg.py
│   ├── models.py
│   └── admin.py
│
├── static/                        # Arquivos estáticos
│   ├── css/
│   │   ├── input.css              # Input Tailwind
│   │   └── styles.css             # Output compilado
│   ├── img/                       # Imagens
│   └── javascript/
│       ├── system-analysis.js
│       ├── num-converter.js
│       └── register.js
│
├── docs/                          # Documentação
│   ├── index.md
│   ├── overview.md
│   ├── installation.md
│   ├── configuration.md
│   ├── architecture.md
│   ├── project-structure.md
│   ├── authentication.md
│   ├── security.md
│   ├── api-reference.md
│   ├── guidelines.md
│   ├── contributing.md
│   ├── development.md
│   ├── tools.md
│   ├── prerequisites.md
│   └── release-notes.md
│
├── .gitignore
├── .env.example
├── build-tailwind.sh
├── manage.py
├── README.md
├── requirements.txt
├── requirements_dev.txt
├── tailwind.config.js
├── db.sqlite3                     # Banco (dev only)
└── venv/                          # Ambiente virtual (ignorado)
```

---

## Arquivos Principais

### core/settings.py

Configurações centrais do Django:

- `SECRET_KEY`: Chave de segurança
- `DEBUG`: Modo debug
- `INSTALLED_APPS`: Apps registradas
- `MIDDLEWARE`: Middlewares ativas
- `TEMPLATES`: Configuração de templates
- `DATABASES`: Banco de dados

**Quando editar**: Adicionar apps, configurar variáveis, modificar middlewares.

---

### core/urls.py

Rotas globais:

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('accounts/', include('users.urls')),
    path('sistema/', include('tools.urls')),
]
```

---

### users/forms.py

Formulários customizados para registro:

- `CustomUserCreationForm`: Valida username, email, senha
- `clean_email()`: Bloqueia emails temporários
- `clean_username()`: Verifica duplicação

---

### users/models.py

Modelos:

- `TermsOfUseAndPrivacyPolicy`: Histórico de termos

---

### users/signals.py

Quando usuário é criado, dispara `send_new_user_email()`.

---

### tools/views.py

**Template Views**:

- `SystemAnalysisView`: Dashboard monitoramento
- `NumberConverterView`: Página conversor

**API Views**:

- `SystemAnalysisAPIView`: GET `/sistema/monitoramento/v1/metrics-api`
- `AiAPIView`: GET `/sistema/monitoramento/v1/ai-api`
- `NumberConverterAPIView`: GET `/sistema/conversor/v1/api`

---

### tools/services/system_metrics.py

Coleta de métricas:

```python
def get_system_status():
    """Retorna dict com cpu_percent, ram_percent, etc."""
    
def sanitize_system_data(status):
    """Normaliza para high/normal para IA."""
```

---

### tools/services/ai_analysis.py

Integração Groq:

```python
def get_ai_analysis():
    """Coleta dados, sanitiza, chama Groq."""
```

---

### tools/services/num_converter.py

Conversões numéricas:

```python
bin_to_dec(binary: str) -> int
dec_to_bin(decimal: int) -> str
hex_to_dec(hex: str) -> int
dec_to_hex(decimal: int) -> str
oct_to_dec(oct: str) -> int
dec_to_oct(decimal: int) -> str
```

---

### notifications/utils/send_email.py

Lógica de envio:

```python
def send_new_user_email(user):
    """Envia email de boas-vindas."""
    
def send_update_terms_email(user):
    """Notifica atualização de termos."""
```

---

### notifications/utils/email_oauth2.py

Autenticação OAuth2 Google:

```python
def get_oauth2_string(email, client_id, client_secret, refresh_token):
    """Retorna string XOAUTH2 para SMTP."""
```

---

### static/javascript/system-analysis.js

Dashboard de monitoramento:

```javascript
async function getSystemMetrics()
    // Requisita API a cada 5s
    
async function aiAnalysis()
    // Requisita análise IA
```

---

### static/javascript/num-converter.js

Conversor numérico:

```javascript
async function converter()
    // Requisita conversão
    
async function boolean()
    // Operações lógicas
```

---

### build-tailwind.sh

Script para compilar Tailwind CSS:

```bash
bash build-tailwind.sh
```

Execute quando modificar `static/css/input.css`.

---

### requirements.txt

Dependências do projeto. Instale com:

```bash
pip install -r requirements.txt
```

---

### tailwind.config.js

Configuração do Tailwind CSS. Escaneia templates para classes usadas.

---

## Convenções de Nomenclatura

### Python

- **Classes**: `PascalCase` → `SystemAnalysisView`
- **Funções**: `snake_case` → `get_system_status()`
- **Variáveis**: `snake_case` → `cpu_percent`
- **Constantes**: `UPPER_SNAKE_CASE` → `API_TIMEOUT`

### HTML/CSS

- **Classes Tailwind**: `kebab-case` → `bg-purple-500`, `text-white`
- **IDs**: `snake_case` → `cpu_meter`
- **Data attributes**: `kebab-case` → `data-system-id`

### JavaScript

- **Funções**: `camelCase` → `getSystemMetrics()`
- **Variáveis**: `camelCase` → `cpuValue`
- **Constantes**: `UPPER_SNAKE_CASE` → `API_ENDPOINT`

### Arquivos

- **Python**: `snake_case.py` → `system_metrics.py`
- **HTML**: `snake_case.html` → `system_analysis.html`
- **JavaScript**: `kebab-case.js` → `system-analysis.js`

---

## Fluxo de Adição de Novo Recurso

Exemplo: Adicionar novo endpoint para RAM apenas.

### 1. Criar função no service

```python
# tools/services/system_metrics.py
def get_ram_only():
    ram = psutil.virtual_memory()
    return {
        'ram_percent': ram.percent,
        'ram_total': round(ram.total / (1024**3), 2),
        'ram_used': round(ram.used / (1024**3), 2)
    }
```

### 2. Criar view

```python
# tools/views.py
class RamOnlyAPIView(LoginRequiredMixin, generic.View):
    def get(self, request):
        data = get_ram_only()
        return JsonResponse({'data': data})
```

### 3. Adicionar rota

```python
# tools/urls.py
path('ram/', RamOnlyAPIView.as_view(), name='ram_only_api')
```

### 4. Usar no frontend

```javascript
fetch('/sistema/ram/')
    .then(r => r.json())
    .then(data => console.log(data))
```

---

## Próximas Etapas

- [Arquitetura](./architecture.md) - Design técnico
- [Desenvolvimento](./development.md) - Workflow local
