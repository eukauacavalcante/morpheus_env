# Guia de Contribuição

Agradecemos o seu interesse em contribuir com o projeto. Esta página dará a você uma breve visão geral de como as coisas são organizadas e, mais importante, como participar. Todos são bem-vindos para contribuir e valorizamos cada contribuição.

---

## Começar

### 1. Fork e Clone

```bash
# No GitHub, clique em "Fork"
git clone https://github.com/SEU_USERNAME/morpheus_env.git
cd morpheus_env
```

### 2. Criar Branch

```bash
git checkout -b feature/minha-feature
# ou
git checkout -b fix/meu-bug
# ou
git checkout -b docs/melhorias
```

**Padrões de branch**:

- `feature/`: Nova funcionalidade
- `fix/`: Correção de bug
- `docs/`: Melhorias na documentação

### 3. Fazer Alterações

Siga [Guidelines](./guidelines.md) para padrões de código.

```bash
# Testar
python manage.py runserver
python manage.py test

# Verificar qualidade
flake8 .
isort . --check-only
```

### 4. Commit com Mensagem Clara

```bash
git add .
git commit -m "feat: Descrição do que mudou"
```

**Tipos de commit** (Conventional Commits):

- `feat`: Nova funcionalidade
- `fix`: Correção de bug
- `docs`: Documentação
- `test`: Testes
- `refactor`: Reorganização

### 5. Push e Pull Request

```bash
git push origin feature/minha-feature
```

No GitHub: criar PR para branch `develop` (não `main`).

**Template PR**:

```markdown
## Descrição
Breve descrição do que foi implementado.

## Tipo
- [ ] Bug fix
- [ ] Nova funcionalidade
- [ ] Documentação

## Checklist
- [ ] Código segue guidelines
- [ ] Testes adicionados
- [ ] Documentação atualizada
- [ ] Sem conflitos com base
- [ ] Commits com mensagens claras
```

---

## Tipos de Contribuição

### Bug Fixes

Corrigir comportamento inesperado.

```bash
git checkout -b fix/nome-do-bug
# Editar e testar
git commit -m "fix: Descrever correção"
```

---

### Novas Funcionalidades

Adicionar novo recurso.

**Exemplo: Novo endpoint de API**

```python
# tools/services/new_service.py
def get_new_metric():
    """Coleta nova métrica."""
    return {'data': 'valor'}

# tools/views.py
class NewMetricAPIView(LoginRequiredMixin, generic.View):
    def get(self, request):
        data = get_new_metric()
        return JsonResponse({'data': data})

# tools/urls.py
path('new-metric/', NewMetricAPIView.as_view(), name='new_metric_api')
```

Adicione testes e atualize documentação.

---

### Melhorias na Documentação

Adicionar ou melhorar docs.

```bash
git checkout -b docs/melhorias-docs
# Editar arquivos .md em /docs/
git commit -m "docs: Descrever melhoria"
```

---

### Testes

Adicionar testes para funcionalidades.

```python
# tools/tests.py
from django.test import TestCase

class SystemMetricsTests(TestCase):
    def test_get_system_status(self):
        """Testa coleta de métricas."""
        data = get_system_status()
        self.assertIn('cpu_percent', data)
```

Executar:

```bash
python manage.py test tools.tests.SystemMetricsTests
```

---

## Processo de Review

### Checklist de Review

PR será revisado verificando:

- Código segue [Guidelines](./guidelines.md)
- Sem conflitos com base
- Testes adicionados/atualizados
- Documentação atualizada
- Mensagens de commit claras
- Sem secrets hardcoded
- Seguro (validação, injeção, etc)

### Responder a Feedback

Se feedback for solicitado:

```bash
# Fazer ajustes
nano file.py

# Commit do ajuste
git add .
git commit -m "refactor: Ajustar conforme feedback"

# Push novamente
git push origin feature/minha-feature

# ⚠️ Não use --force em PRs públicos
```

---

## Setup Local

```bash
# Clonar seu fork
git clone https://github.com/SEU_USERNAME/morpheus_env.git
cd morpheus_env

# Criar venv
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate (Windows)

# Instalar dependências
pip install -r requirements.txt
pip install -r requirements_dev.txt

# Criar .env
cp .env.example .env
# Edite com DEBUG=True, EMAIL_MODE=False, AI_MODE=False

# Banco de dados
python manage.py migrate
python manage.py createsuperuser

# Servidor
python manage.py runserver
```

---

## Problemas Comuns

### Branch divergiu de develop

```bash
git fetch origin
git rebase origin/develop
# Se conflitos: resolver e git rebase --continue
```

### PR não aparece para merge

Pode haver conflitos. Verifique:

```bash
git merge origin/develop
```

---

## Boas Práticas

### ✅ Fazer

- Commits pequenos e focados
- Descrições detalhadas de PR
- Testar localmente antes de pushar
- Responder a feedback construtivamente
- Atualizar documentação
- Usar branch `develop`, não `main`

### ❌ Não Fazer

- Force push em PRs públicos
- Misturar múltiplas features
- Ignorar testes falhos
- Commitar secrets
- Ignorar feedback

---

## Comunidade

- Email: morpheusenv@gmail.com
- GitHub Issues: [Reportar bugs](https://github.com/eukauacavalcante/morpheus_env/issues)
- GitHub Discussions: [Sugestões](https://github.com/eukauacavalcante/morpheus_env/discussions)

**Obrigado por contribuir!**
