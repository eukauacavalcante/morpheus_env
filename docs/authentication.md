# Autenticação e Controle de Acesso

Sistema de autenticação do Morpheus Env com validações customizadas.

---

## Fluxo de Autenticação do Morpheus

### Registro de Usuário

**Validações Customizadas** (`users/forms.py`):

1. **Nome**: Automaticamente capitalizado
2. **Username**: Não pode ser duplicado ou apenas números
3. **Email**: Bloqueio de domínios temporários (blocklist em `users/validators/disposable_email_blocklist.conf`)
4. **Senha**: Validadores built-in do Django (8 caracteres mín, força)

**Fluxo**:
```
POST /accounts/registrar/
    ↓
CustomUserCreationForm valida
    ├─ clean_username() - verifica duplicação e formato
    ├─ clean_email() - bloqueia emails temporários
    └─ clean_password*() - valida força
    ↓
User criado no banco
    ↓
Signal post_save dispara
    ↓
send_new_user_email() (se EMAIL_MODE=True)
```

**Bloqueio de Emails Temporários**:

O arquivo `users/validators/disposable_email_blocklist.conf` contém domínios bloqueados:
```
tempmail.com
guerrillamail.com
10minutemail.com
```

Adicione novos domínios conforme necessário.

---

### Login

Usa `LoginView` padrão do Django com proteção CSRF.

**Request**:
```
POST /accounts/login/
username=joao&password=senha123&csrfmiddlewaretoken=abc123
```

**Response**: Sessão criada (cookie HttpOnly `sessionid`)

---

### Logout

Usa `LogoutView` padrão do Django. Remove sessão do banco.

**Request**:
```
POST /accounts/logout/
csrfmiddlewaretoken=abc123
```

---

## Proteção de Acesso a Views

### LoginRequiredMixin

Restringe acesso apenas para usuários autenticados.

**Implementação no Morpheus**:

```python
# core/views.py
class HomeView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'index.html'

# tools/views.py
class SystemAnalysisView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'system_analysis.html'

# users/views.py
class TermsOfUseView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'terms_of_use.html'
```

Se não autenticado: Redirect para `/accounts/login/?next=/original-url/`

---

### Acessar Usuário em Views

```python
def my_view(request):
    if request.user.is_authenticated:
        username = request.user.username
        email = request.user.email
```

Em templates:
```html
{% if user.is_authenticated %}
    <p>Olá, {{ user.first_name }}!</p>
{% endif %}
```

---

## Sinais de Autenticação

Quando um novo usuário é criado, um signal dispara automaticamente:

```python
# users/signals.py
@receiver(post_save, sender=User)
def send_email_user(sender, instance, created, **kwargs):
    if created:  # Apenas para novo usuário
        send_new_user_email(instance)
```

Este sinal envia email de boas-vindas (se `EMAIL_MODE=True`).

**Registro do signal** (`users/apps.py`):
```python
def ready(self):
    import users.signals
```

---

## Modelo de Dados de Usuário

O Django fornece `User` padrão. O Morpheus adiciona:

**TermsOfUseAndPrivacyPolicy** (`users/models.py`):

```python
class TermsOfUseAndPrivacyPolicy(models.Model):
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
```

Permite histórico de termos sem redeploy.

---

## Rate Limiting em Login

**Status**: Não implementado

**Recomendação**: Instalar `django-axes` para prevenir força bruta

```bash
pip install django-axes
```

Configurar em `settings.py`:
```python
INSTALLED_APPS += ['axes']
MIDDLEWARE += ['axes.middleware.AxesMiddleware']

AXES_FAILURE_LIMIT = 5
AXES_COOLOFF_TIME = timedelta(minutes=30)
```

---

## Boas Práticas

- Sempre validar entrada (email, username, senha)
- Usar `LoginRequiredMixin` em views protegidas
- Testar autenticação em desenvolvimento com `python manage.py shell`
- Implementar django-axes em produção