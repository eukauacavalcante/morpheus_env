# Segurança do Morpheus Env

Documentação completa de implementações de segurança, proteções e boas práticas no Morpheus Env.

---

## Proteções Implementadas

### CSRF (Cross-Site Request Forgery)

Todos os formulários incluem token CSRF automaticamente.

**Em templates**:

```html
<form method="post">
    {% csrf_token %}
    <input type="text" name="field">
</form>
```

Django valida automaticamente na submissão.

**Em AJAX**:

```javascript
const token = document.querySelector('[name=csrfmiddlewaretoken]').value;
fetch('/api/endpoint/', {
    method: 'POST',
    headers: {
        'X-CSRFToken': token,
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({...})
});
```

---

### XSS (Cross-Site Scripting)

Templates escapam HTML por padrão:

```html
<!-- ✅ Seguro (Django escapa automaticamente) -->
<p>{{ user_input }}</p>

<!-- Entrada: <script>alert('XSS')</script> -->
<!-- Output: <p>&lt;script&gt;alert('XSS')&lt;/script&gt;</p> -->

<!-- ❌ NUNCA usar |safe com dados de usuário -->
<p>{{ user_input|safe }}</p>
```

---

### SQL Injection

Sempre use Django ORM:

```python
# ✅ Seguro
user = User.objects.filter(username=username).first()

# ❌ NUNCA fazer isto
user = User.objects.raw(f"SELECT * FROM auth_user WHERE username='{username}'")
```

---

### Validação de Email

O Morpheus bloqueia emails temporários/descartáveis.

**Arquivo**: `users/validators/disposable_email_blocklist.conf`

Domínios bloqueados (um por linha):

```
tempmail.com
guerrillamail.com
10minutemail.com
```

**Validação no registro** (`users/forms.py`):

```python
def clean_email(self):
    email = self.cleaned_data.get('email')
    domain = email.split('@')[1].lower()
    
    with importlib.resources.open_text(
        'users.validators',
        'disposable_email_blocklist.conf'
    ) as f:
        blocklist = {line.strip().lower() for line in f}
    
    if domain in blocklist:
        raise ValidationError('E-mails temporários não são permitidos.')
    
    return email
```

---

### Senhas com Hash Seguro

Django usa PBKDF2 com 260.000 iterações por padrão.

**Criar usuário**:

```python
user = User.objects.create_user(
    username='joao',
    email='joao@example.com',
    password='senha123'
)
# Senha é hasheada automaticamente
```

**Verificar senha**:

```python
user.check_password('senha123')  # True
```

**Nunca armazene em texto plano.**

---

### Rate Limiting

Protege endpoints contra abuso.

**Configuração** (`tools/views.py`):

```python
@method_decorator(ratelimit(key='user', rate='20/m', method='GET'), name='dispatch')
class SystemAnalysisAPIView(LoginRequiredMixin, generic.View):
    # 20 requisições/minuto por usuário
    pass
```

**Limites atuais**:

- Métricas do sistema: 20/minuto (CPU-intensive)
- Análise de IA: 10/minuto (API cara)
- Conversor: Sem limite (operação leve)

**Response ao exceder limite**:

```
HTTP 429 Too Many Requests
```

---

### Proteção de Sessão

Configurações em `core/settings.py`:

```python
SESSION_COOKIE_SECURE = False  # True em produção (HTTPS)
SESSION_COOKIE_HTTPONLY = True  # Não acessível via JS
SESSION_EXPIRE_AT_BROWSER_CLOSE = True  # Expira ao fechar navegador
```

---

## Variáveis Sensíveis

Nunca armazene secrets no código:

**❌ NUNCA fazer isto**:

```python
SECRET_KEY = 'django-insecure-abc123xyz789'
API_KEY = 'gsk_abc123xyz789'
EMAIL_PASSWORD = 'senha123'
```

**✅ Usar .env**:

```env
SECRET_KEY=django-insecure-abc123xyz789
API_KEY=gsk_abc123xyz789
EMAIL_HOST_PASSWORD=senha123
```

**Carregamento seguro**:

```python
from decouple import config

SECRET_KEY = config('SECRET_KEY')
API_KEY = config('API_KEY')
```

---

## Checklist de Segurança

Antes de fazer deploy:

- [ ] `DEBUG=False` em produção
- [ ] `SECRET_KEY` alterada
- [ ] `ALLOWED_HOSTS` configurado
- [ ] HTTPS ativado
- [ ] Cookies com `SECURE` e `HTTPONLY`
- [ ] Rate limiting em endpoints sensíveis
- [ ] Validação de input em formulários
- [ ] CSRF protection ativo
- [ ] XSS prevention (auto-escape)
- [ ] Sem secrets hardcoded
- [ ] Nenhum print/log de dados sensíveis
- [ ] Email validado (bloqueia temporários)
- [ ] Senhas com hash forte

---

## Vulnerabilidades Conhecidas e Mitigações

### Força Bruta em Login

**Status**: Não implementado

**Solução**: Instalar `django-axes`

```bash
pip install django-axes
```

Configure em `settings.py`:

```python
INSTALLED_APPS += ['axes']
MIDDLEWARE += ['axes.middleware.AxesMiddleware']

AXES_FAILURE_LIMIT = 5
AXES_COOLOFF_TIME = timedelta(minutes=30)
```

---

### Rate Limiting sem Cache

**Status**: Implementado

Limita por usuário autenticado. Sem cache em desenvolvimento.

**Para produção**: Considerar Redis para cache de rate limiting.

---

## Boas Práticas

### ✅ Fazer

- Validar entrada de usuário sempre
- Usar Django ORM
- Escape em templates (automático)
- Usar HTTPS em produção
- Implementar rate limiting
- Usar variáveis de ambiente para secrets
- Verificar logs de segurança
- Manter dependências atualizadas

### ❌ Não Fazer

- Hardcode secrets no código
- Confiar em dados do cliente
- Construir SQL manualmente
- Desabilitar CSRF
- Usar `DEBUG=True` em produção
- Compartilhar chaves
- Ignorar warnings de segurança
- Deixar senhas em logs

---

## Próximas Etapas

- [Guidelines](./guidelines.md) - Padrões de código seguro
- [Autenticação](./authentication.md) - Sistema de autenticação
- [Contribuição](./contributing.md) - Como contribuir
