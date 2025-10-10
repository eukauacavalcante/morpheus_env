# Morpheus Env

<div align="center">

![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-blue)
![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Django](https://img.shields.io/badge/Django-5.2-darkgreen?logo=django)
![License](https://img.shields.io/badge/License-GNU-blue)

**Simulador de Sistema Computacional Seguro** 🔐

Um projeto acadêmico e experimental para monitoramento de sistema com análise por IA e ferramentas computacionais.

</div>

## 🎯 Visão Geral

**Morpheus Env** é um simulador web que oferece ferramentas educacionais para análise de sistemas computacionais. O projeto foi desenvolvido com fins **experimentais e acadêmicos**, voltado à pesquisa, aprendizado e demonstração de conceitos.

> ⚠️ Os resultados e recursos do sistema não devem ser interpretados como serviços profissionais ou comerciais.

### Principais Funcionalidades

- 📊 **Monitoramento de Sistema** com análise em tempo real (CPU, RAM, Disco)
- 🤖 **Análise por IA** usando Groq AI para insights sobre o desempenho
- 🔢 **Conversor Numérico** com suporte para binário, hexadecimal, octal e decimal
- ⚡ **Operações Lógicas** (AND, OR, XOR) para trabalhar com valores booleanos
- 🔐 **Autenticação Segura** com validação de email temporário
- 📧 **Sistema de Notificações** por email com OAuth2 do Google
- 🎨 **Interface Moderna** com Tailwind CSS e efeitos glassmorphism

---

## ⭐ Features

### Autenticação e Usuários
- ✅ Registro de usuários com validação forte
- ✅ Bloqueio de emails temporários/descartáveis
- ✅ Senhas com hash seguro (Django)
- ✅ Logout seguro

### Monitoramento do Sistema
- ✅ Coleta de métricas em tempo real (CPU, RAM, Disco)
- ✅ Análise de desempenho via IA
- ✅ Interface de dashboard responsiva

### Conversão Numérica e Lógica Booleana
- ✅ Conversão entre bases numéricas (2, 8, 10, 16)
- ✅ Operações lógicas booleanas
- ✅ Validação de entrada robusta
- ✅ Respostas via API

### Notificações
- ✅ Emails de boas-vindas para novos usuários
- ✅ Notificações de atualização de termos
- ✅ Autenticação OAuth2 com Google
- ✅ Mensagens coloridas no terminal

---

## 🛠 Stack Tecnológica

### Backend
- **Python 3.12** - Linguagem de programação
- **Django 5.2** - Framework web
- **SQLite** - Banco de dados (desenvolvimento)
- **Groq AI** - Análise inteligente de métricas

### Frontend
- **Django Templates** - Renderização de página
- **Tailwind CSS** - Estilização com utility-first
- **JavaScript Vanilla** - Interatividade
- **Bootstrap Icons** - Ícones

### Ferramentas Externas
- **Google OAuth2** - Autenticação e envio de emails
- **psutil** - Coleta de métricas do sistema
- **colorama** - Mensagens coloridas no terminal
- **python-decouple** - Gerenciamento de variáveis de ambiente

---

## 📦 Instalação

### Pré-requisitos
- Python 3.13+
- pip (gerenciador de pacotes Python)
- Git

### Passo 1: Clonar o Repositório

```bash
git clone https://github.com/eukauacavalcante/morpheus_env.git
cd morpheus_env
```

### Passo 2: Criar Ambiente Virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Passo 3: Instalar Dependências

```bash
pip install -r requirements.txt
```

### Passo 4: Configurar Variáveis de Ambiente

**ATENÇÃO**: Se o AI_MODE e EMAIL_MODE estiverem desativados (False), você não precisará realizar as configurações de IA e Email. As funcionalidades citadas estarão indisponíveis.

Crie um arquivo `.env` na raiz do projeto:

```env
# Django
SECRET_KEY=sua-chave-secreta-aqui
DEBUG=True
ALLOWED_HOSTS=[localhost,127.0.0.1]

# Database (optional - padrão é SQLite)
DATABASE_URL=sqlite:///db.sqlite3

# IA - Groq
API_KEY=sua-chave-groq-aqui
AI_MODEL=mixtral-8x7b-32768
AI_MODE=False

# Email
EMAIL_MODE=False
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=seu-email@gmail.com
EMAIL_HOST_PASSWORD=sua-senha-app
DEFAULT_FROM_EMAIL=seu-email@gmail.com

# Google OAuth2
GOOGLE_OAUTH2_CLIENT_ID=seu-client-id
GOOGLE_OAUTH2_CLIENT_SECRET=seu-client-secret
GOOGLE_OAUTH2_REFRESH_TOKEN=seu-refresh-token
```

### Passo 5: Migrar Banco de Dados

```bash
python manage.py migrate
```

### Passo 6: Criar Superusuário (Admin)

```bash
python manage.py createsuperuser
```

### Passo 7: Executar o Servidor

```bash
python manage.py runserver
```

Acesse: http://localhost:8000

## ⚙️ Configuração

### Variáveis de Ambiente Detalhadas

| Variável | Descrição | Exemplo |
|----------|-----------|---------|
| `SECRET_KEY` | Chave secreta Django | `django-insecure-...` |
| `DEBUG` | Modo debug | `True` ou `False` |
| `AI_MODE` | Ativa análise por IA | `True` ou `False` |
| `EMAIL_MODE` | Ativa envio de emails | `True` ou `False` |
| `API_KEY` | Chave da API Groq | Obter em groq.com |
| `AI_MODEL` | Modelo de IA a usar | `mixtral-8x7b-32768` |

## 🏗 Arquitetura

### Padrão MVC

O projeto segue o padrão MVT (Model-View-Template) do Django:

- **Models** (`models.py`) - Estrutura de dados
- **Views** (`views.py`) - Lógica de negócio e requisições
- **Templates** (`templates/`) - Apresentação de dados

---

## 📱 Apps Django

### 1. **users** - Autenticação e Perfil
Responsável por gerenciar usuários, autenticação e termos de uso.

### 2. **tools** - Ferramentas do Sistema
Oferece monitoramento de sistema e ferramentas computacionais.

### 3. **notifications** - Notificações e Emails
Gerencia notificação via email com autenticação segura.

---

## 📚 Documentação

### Links Úteis

- [Documentação Django](https://docs.djangoproject.com/)
- [Tailwind CSS Docs](https://tailwindcss.com/docs)
- [Groq API Docs](https://console.groq.com/docs)
- [Google OAuth2 Setup](https://developers.google.com/identity/protocols/oauth2)

---

## 📝 Licença

Este projeto está licenciado sob a Licença GNU GENERAL PUBLIC LICENSE - veja o arquivo [LICENSE](LICENSE) para detalhes.

---

## ⚠️ Avisos Importantes

Este é um **projeto acadêmico e experimental**. 

- Não use em produção
- Não interprete os resultados como análises profissionais
- Para fins educacionais apenas

---

## 🤝 Contribuições

Contribuições são bem-vindas! Para contribuir:

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Add MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abra um Pull Request

---

## 📧 Suporte

Para reportar bugs ou sugerir melhorias, entre em contato:

📧 **Email**: morpheusenv@gmail.com

---

<div align="center">

**Desenvolvido para educação e experimentação**

*Morpheus Env © 2025 - Projeto Acadêmico e Experimental*

</div>