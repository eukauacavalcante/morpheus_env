# Visão Geral do Projeto

## O que é Morpheus Env?

**Morpheus Env** é um simulador web de sistema computacional desenvolvido com fins **experimentais e acadêmicos**. O projeto foi criado para oferecer ferramentas educacionais que permitem aos usuários aprender e experimentar conceitos de monitoramento de sistema, conversão numérica e operações lógicas booleanas.

O nome "Morpheus" é uma referência ao deus do sonho da mitologia grega, onde seu trabalho é simular uma realidade através dos sonhos das pessoas enquanto elas dormem. Neste contexto, o sistema oferece diferentes "visualizações" da realidade computacional.

---

## Objetivo do Projeto

Fornecer uma plataforma educacional que combine:

1. **Monitoramento em Tempo Real**: Observar métricas do sistema (CPU, RAM, Disco)
2. **Análise Inteligente**: Utilizar IA para interpretar dados de desempenho
3. **Ferramentas Educacionais**: Conversores numéricos e operações lógicas
4. **Segurança Prática**: Implementar autenticação e validação de dados

---

## Principais Funcionalidades

### 1. Monitoramento do Sistema

Coleta e exibe em tempo real:

- **CPU**: Porcentagem de uso do processador
- **RAM**: Memória disponível e em uso
- **Disco**: Espaço de armazenamento utilizado

Os dados são atualizados a cada 5 segundos via API REST.

### 2. Análise por IA

O sistema utiliza **Groq AI** para gerar análises automáticas do desempenho:

- Interpreta níveis de CPU e RAM
- Fornece alertas quando recursos estão críticos
- Sugere ações preventivas
- Retorna análise em um parágrafo único e conciso

### 3. Conversor Numérico

Converte números entre diferentes bases:

- **Binário** (base 2): 1010
- **Octal** (base 8): 12
- **Decimal** (base 10): 10
- **Hexadecimal** (base 16): A

Suporta conversões bidirecionais entre todas as bases.

### 4. Operações Lógicas Booleanas

Implementa operações fundamentais:

- **AND**: Retorna 1 apenas se ambos os valores são 1
- **OR**: Retorna 1 se pelo menos um valor é 1
- **XOR**: Retorna 1 se os valores são diferentes

### 5. Autenticação e Segurança

- Registro de usuários com validação forte
- Bloqueio de emails temporários/descartáveis
- Senhas com hash seguro usando padrões Django
- Sistema de logout seguro
- Autenticação JWT stateless com access/refresh tokens
- Access tokens válidos por 10 minutos
- Refresh tokens válidos por 1 dia
- Validação de CSRF em todos os formulários

### 6. Notificações por Email

- Emails de boas-vindas para novos usuários
- Notificações de atualização de termos
- Autenticação OAuth2 com Google
- Mensagens formatadas em HTML e texto plano

---

## Stack Tecnológica

### Backend
- **Python 3.12**: Linguagem de programação
- **Django 5.2.6**: Framework web robusto
- **Django REST Framework 3.16.1**: Construção de APIs REST
- **SQLite**: Banco de dados (desenvolvimento)
- **Groq AI**: API de análise inteligente
- **psutil**: Coleta de métricas do sistema
- **google-auth**: OAuth2 para Google
- **djangorestframework-simplejwt**: Autenticação JWT para APIs REST

### Frontend
- **Django Templates**: Renderização de páginas
- **Tailwind CSS**: Estilização utility-first
- **DaisyUI Components**: Conjunto de componentes
- **Bootstrap Icons**: Conjunto de ícones
- **JavaScript Vanilla**: Interatividade sem dependências pesadas

### Deployment e Ferramentas
- **Git**: Controle de versão
- **Virtual Environment**: Isolamento de dependências
- **pip**: Gerenciador de pacotes Python

---

## Arquitetura Geral

``` mermaid

flowchart LR
    A["🌐 Cliente<br/>Navegador"] -->|HTTP| B["⚙️ Django<br/>Backend"]
    B -->|Consulta| C["💾 SQLite"]
    B -->|API| D["🤖 Groq AI"]
    B -->|Monitoramento| E["📊 psutil"]
    B -->|Conversão| F["🔢 Conversor<br/>Numérico/Lógico"]
    B -->|Resposta| A

    style A stroke:#0288d1,stroke-width:2px,color:#000
    style B stroke:#7b1fa2,stroke-width:2px,color:#000
    style C stroke:#f9a825,stroke-width:2px,color:#000
    style D stroke:#00897b,stroke-width:2px,color:#000
    style E stroke:#e64a19,stroke-width:2px,color:#000
    style F stroke:#5e35b1,stroke-width:2px,color:#000
```

---

## Fluxo de Dados

### Monitoramento do Sistema

1. Usuário acessa `/sistema/monitoramento/`
2. Frontend requisita dados via `/sistema/monitoramento/api/v1/metrics`
3. Django executa `get_system_status()` do `psutil`
4. Retorna JSON com métricas (CPU, RAM, Disco)
5. Frontend atualiza a cada 5 segundos

### Análise de IA

1. Usuário clica no botão "Gerar análise"
2. Frontend requisita `/sistema/monitoramento/api/v1/ai`
3. Django executa `get_ai_analysis()` da Groq
4. Groq recebe dados sanitizados e retorna análise em texto
5. Frontend exibe análise no painel

### Conversão Numérica

1. Usuário preenche valor e seleciona conversão
2. Frontend requisita `/sistema/conversor/api/v1/converter?type=bin2dec&value=1010`
3. Django mapeia operação para função correspondente
4. Retorna resultado em JSON
5. Frontend exibe resultado

---

## Padrão de Projeto: MVT

O projeto segue rigorosamente o padrão **MVT (Model-View-Template)** do Django:

- **Models**: Definem a estrutura de dados no banco (ORM Django)
- **Views**: Contêm a lógica de negócio e processamento de requisições
- **Templates**: Renderizam HTML com dados do contexto

Exemplo:
```python
# models.py - Define estrutura
class TermsOfUseAndPrivacyPolicy(models.Model):
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

# views.py - Lógica de negócio
class TermsOfUseView(generic.TemplateView):
    def get_context_data(self):
        terms = TermsOfUseAndPrivacyPolicy.objects.filter(is_active=True).last()
        return {'terms_and_policy': terms}

# templates/terms_of_use.html - Renderização
{{ terms_and_policy }}
```

---

## Módulos Principais

### Apps Django

#### 1. **users** - Autenticação e Usuários
Gerencia registro, login e termos de uso.

#### 2. **tools** - Ferramentas do Sistema
Oferece monitoramento, análise de IA e conversores.

#### 3. **notifications** - Notificações e Emails
Envia emails via OAuth2 Google.

### Estrutura de Serviços

```
tools/services/
├── num_converter.py      # Lógica de conversão numérica
├── system_metrics.py     # Coleta de métricas do sistema
└── ai_analysis.py        # Integração com Groq AI

notifications/utils/
├── email_oauth2.py       # Autenticação OAuth2 Google
├── send_email.py         # Envio de emails
├── colors.py             # Mensagens coloridas no terminal
└── emails.py             # Templates de email
```

---

## Segurança e Conformidade

### Implementações de Segurança

1. **Proteção CSRF**: Todos os formulários incluem token CSRF
2. **Autenticação por Login**: Decoradores `LoginRequiredMixin` em views
3. **Rate Limiting**: Limitação de requisições por usuário (20/minuto para métricas)
4. **Django Axes**: Limitação de tentativas de login (5 tentativas disponíveis)
5. **Validação de Email**: Bloqueio de domínios temporários
6. **Hash de Senha**: Django utiliza PBKDF2 por padrão
7. **Variáveis de Ambiente**: Senhas e API keys em `.env` (não versionadas)

### Validações

- Emails descartáveis são bloqueados no registro
- Senhas requerem mínimo 8 caracteres
- Nomes de usuário não podem ser apenas numéricos
- Entradas sanitizadas antes de processar em IA

---

## Fluxo de Usuário

### Novo Usuário

1. Acessa `/accounts/registrar/`
2. Preenche formulário com nome, usuário, email e senha
3. Validações verificam:

    - Email não é temporário
    - Usuário não existe
    - Senha atende requisitos

4. Usuário criado e email de boas-vindas enviado
5. Redirecionado para login

### Usuário Autenticado

1. Faz login em `/accounts/login/`
2. Acessa a home em `/`
3. Pode utilizar ferramentas disponíveis
4. Faz logout em qualquer página

---

## Limitações Conhecidas

- ⚠️ SQLite é inadequado para produção (use PostgreSQL/MySQL)
- ⚠️ Análise de IA requer configuração de API key da Groq
- ⚠️ Emails requerem configuração OAuth2 do Google
- ⚠️ Não há cache implementado

---

## Próximos Passos

Para começar a trabalhar com o projeto, consulte:

- [Pré-requisitos](./prerequisites.md) - Requisitos mínimos
- [Instalação](./installation.md) - Como configurar o ambiente
- [Configuração](./configuration.md) - Variáveis de ambiente
