# Guia de Desenvolvimento Local

Instruções práticas para setup e workflow para desenvolvimento do Morpheus Env.

---

## Setup Inicial

```bash
# 1. Clonar
git clone https://github.com/eukauacavalcante/morpheus_env.git
cd morpheus_env

# 2. Ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/macOS
# ou
venv\Scripts\activate  # Windows

# 3. Dependências
pip install -r requirements.txt
pip install -r requirements_dev.txt

# 4. Configuração
cp .env.example .env
# Edite .env: DEBUG=True, EMAIL_MODE=False, AI_MODE=False

# 5. Banco de dados
python manage.py migrate
python manage.py createsuperuser

# 6. Servidor
python manage.py runserver
```

Acesse: `http://localhost:8000`

---

## Workflow com Git

### Criar Branch

```bash
git checkout -b feature/nome-da-feature
# ou
git checkout -b fix/nome-do-bug
```

### Fazer Alterações

```bash
# Editar arquivos
nano tools/views.py

# Testar localmente
python manage.py runserver

# Fazer commit com mensagem clara
git add .
git commit -m "feat: Descrição do que mudou"
```

### Submeter PR

```bash
git push origin feature/nome-da-feature
```

No GitHub: criar Pull Request para branch `develop` (não `main`).

---

## Debugging

### Django Shell

```bash
python manage.py shell
```

Dentro do shell:

```python
from django.contrib.auth.models import User
from tools.services import system_metrics

# Testar coleta de métricas
metrics = system_metrics.get_system_status()
print(f"CPU: {metrics['cpu_percent']}%")

# Testar queries
user = User.objects.get(username='joao')
print(user.email)
```

### Print Debugging

```python
# Em views ou services
print(f"CPU: {cpu_percent}")
print(f"User: {request.user.username}")
```

Aparece no terminal do servidor.

### Browser DevTools

Abra F12 para:

- **Network**: Ver requisições HTTP
- **Console**: Erros JavaScript
- **Application**: Cookies/Storage

---

## Testes

```bash
# Todos os testes
python manage.py test

# App específica
python manage.py test users

# Teste específico
python manage.py test users.tests.UserTests.test_user_created

# Com verbosity
python manage.py test --verbosity=2
```

### Escrever Testes

```python
# users/tests.py
from django.test import TestCase
from django.contrib.auth.models import User

class UserTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
    
    def test_user_created(self):
        """Testa criação de usuário."""
        self.assertEqual(self.user.username, 'testuser')
        self.assertTrue(self.user.is_active)
    
    def test_password_hashed(self):
        """Testa que senha está com hash."""
        self.assertTrue(self.user.check_password('testpass123'))
```

---

## Performance e Otimização

### N+1 Queries Problem

```python
# ❌ RUIM - Query extra para cada usuário
users = User.objects.all()
for user in users:
    print(user.profile.bio)

# ✅ BOM - Uma query
users = User.objects.select_related('profile')
```

### Verificar Queries em Debug

```python
from django.db import connection

users = User.objects.all()
print(f"Total queries: {len(connection.queries)}")
for q in connection.queries:
    print(q['sql'])
```

---

## Compilar CSS

Se modificar Tailwind em `static/css/input.css`:

```bash
bash build-tailwind.sh
```

Ou manualmente:

```bash
source venv/bin/activate
venv/bin/tailwind -i ./static/css/input.css \
                  -o ./static/css/styles.css \
                  --minify
```

---

## Linting

Verificar qualidade de código:

```bash
# flake8
flake8 .
flake8 tools/views.py

# isort (ordernar imports)
isort .

# Verificar sem fazer alterações
isort . --check-only
```

---

## Ambiente de Variáveis

### Desenvolvimento

```env
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
EMAIL_MODE=False
AI_MODE=False
SECRET_KEY=desenvolvimento-key
```

### Produção

```env
DEBUG=False
ALLOWED_HOSTS=example.com,www.example.com
EMAIL_MODE=True
AI_MODE=True
SECRET_KEY=super-secreto-muito-seguro
```

---

## Troubleshooting

### Port 8000 em uso

```bash
# Usar porta diferente
python manage.py runserver 8001

# Ou matar processo
lsof -i :8000
kill -9 <PID>
```

### Database locked

```bash
# Deletar e recriar
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

### ModuleNotFoundError

```bash
# Verificar se venv está ativado
which python  # Deve mostrar venv/bin/python

# Reinstalar dependências
pip install -r requirements.txt
```

---

## Próximas Etapas

- Leia [Guidelines](./guidelines.md) para padrões de código
- Consulte [Contribuições](./contributing.md) para contribuir
- Veja [Segurança](./security.md) para boas práticas
