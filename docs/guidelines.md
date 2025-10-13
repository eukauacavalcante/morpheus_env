# Guidelines de Código

Padrões de código, estilo e boas práticas para contribuir ao Morpheus Env.

---

## Arquitetura e Padrões

### Padrão da Camada de Serviços

Toda lógica de negócio deve estar em `services/` ou `utils/`, não nas views.

**❌ Evitar**:
```python
class SystemAnalysisView(View):
    def get(self, request):
        cpu = psutil.cpu_percent()
        ram = psutil.virtual_memory()
        # ... 50 linhas de lógica aqui
        return JsonResponse(data)
```

**✅ Fazer**:
```python
# tools/services/system_metrics.py
def get_system_status():
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory()
    return {'cpu_percent': cpu, ...}

# tools/views.py
class SystemAnalysisView(View):
    def get(self, request):
        data = get_system_status()
        return JsonResponse({'data': data})
```

---

### Django Views: Class-Based (CBV) Obrigatório

Sempre use Class-Based Views para consistência.

```python
# ✅ Bom
class SystemAnalysisView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'system_analysis.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = get_system_status()
        return context

# ❌ Evitar Function-Based Views
@login_required
def system_analysis(request):
    pass
```

---

## Segurança em Código

### Validação de Input

Valide **sempre** entrada do usuário em formulários.

```python
# users/forms.py - Exemplo do Morpheus
class CustomUserCreationForm(UserCreationForm):
    def clean_username(self):
        username = self.cleaned_data.get('username')
        
        if User.objects.filter(username=username).exists():
            raise ValidationError('Esse usuário já existe')
        
        if username.isdecimal():
            raise ValidationError('Não é permitido apenas números')
        
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        domain = email.split('@')[1].lower()
        
        # Verifica blocklist de emails temporários
        with importlib.resources.open_text(
            'users.validators',
            'disposable_email_blocklist.conf'
        ) as f:
            blocklist = {line.strip().lower() for line in f}
        
        if domain in blocklist:
            raise ValidationError('E-mails temporários não são permitidos.')
        
        return email
```

### SQL Injection Prevention

Sempre use Django ORM:

```python
# ✅ Seguro
user = User.objects.filter(username=username).first()

# ❌ NUNCA fazer isto
user = User.objects.raw(f"SELECT * FROM auth_user WHERE username='{username}'")
```

### XSS Prevention

Templates escapam HTML por padrão:

```html
<!-- ✅ Seguro (Django escapa automaticamente) -->
<p>{{ user_input }}</p>

<!-- ❌ NUNCA usar |safe com dados de usuário -->
<p>{{ user_input|safe }}</p>
```

### CSRF Protection

Sempre incluir token em formulários:

```html
<!-- ✅ Obrigatório -->
<form method="post">
    {% csrf_token %}
    <input type="text" name="field">
</form>
```

Em AJAX:
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

## Nomes e Convenções

### Python

- **Classes**: `PascalCase` → `SystemAnalysisView`, `CustomUserCreationForm`
- **Funções**: `snake_case` → `get_system_status()`, `send_new_user_email()`
- **Constantes**: `UPPER_SNAKE_CASE` → `API_TIMEOUT`, `MAX_RETRIES`

### HTML/CSS

- **Classes Tailwind**: `kebab-case` → `bg-purple-500`, `text-white`, `p-4`
- **IDs e data attributes**: `kebab-case` → `data-system-id="123"`, `id="cpu-meter"`

### JavaScript

- **Funções**: `camelCase` → `getSystemMetrics()`, `updateUI(data)`
- **Variáveis**: `camelCase` → `cpuValue`, `ramUsed`

---

## Commits

Use Conventional Commits:

```
feat: Adicionar nova funcionalidade
fix: Corrigir bug
docs: Atualizar documentação
refactor: Reorganizar código
test: Adicionar testes
```

Exemplo real:
```bash
git commit -m "feat: Implementar análise por IA com Groq"
git commit -m "fix: Corrigir validação de email temporário"
```

---

## Testes

Adicione testes para funcionalidades novas:

```python
# tools/tests.py
from django.test import TestCase

class SystemMetricsTests(TestCase):
    def test_get_system_status(self):
        """Testa coleta de métricas."""
        data = get_system_status()
        self.assertIn('cpu_percent', data)
        self.assertIn('ram_percent', data)
    
    def test_ai_analysis(self):
        """Testa análise por IA."""
        analysis = get_ai_analysis()
        self.assertIsNotNone(analysis)
        self.assertIsInstance(analysis, str)
```

Executar:
```bash
python manage.py test
python manage.py test tools.tests.SystemMetricsTests.test_get_system_status
```

---

## Checklist Antes de Submeter PR

- [ ] Código segue padrões do Morpheus (Service Layer, CBV, etc)
- [ ] Validações de input adicionadas
- [ ] Sem dados sensíveis em logs/prints
- [ ] Testes adicionados e passando
- [ ] Documentação atualizada
- [ ] Mensagens de commit claras
- [ ] Sem conflitos com base
- [ ] Sem erros de linting (`flake8 .`)

---

## Code Review

Todo PR será revisado verificando segurança e padrões. Feedback é construtivo.

Consulte [Contribuições](./contributing.md) para mais detalhes.
