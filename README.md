# Morpheus Env

<div align="center">

![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-blue)
![Python](https://img.shields.io/badge/Python-3.12-yellow?logo=python)
![Django](https://img.shields.io/badge/Django-5.2-darkgreen?logo=django)
![License](https://img.shields.io/badge/License-GNU-blue)

**Simulador de Sistema Computacional Seguro**

Um projeto acadêmico e experimental para monitoramento de sistema com análise por IA e ferramentas computacionais.

</div>

## 🎯 Visão Geral

**Morpheus Env** é um simulador web que oferece ferramentas educacionais para análise de sistemas computacionais. O projeto foi desenvolvido com fins **experimentais e acadêmicos**, voltado à pesquisa, aprendizado e demonstração de conceitos.

> ⚠️ Os resultados e recursos do sistema não devem ser interpretados como serviços profissionais ou comerciais.

### Principais Funcionalidades

- **Monitoramento de Sistema** com análise em tempo real (CPU, RAM, Disco)
- **Análise por IA** usando Groq AI para insights sobre o desempenho
- **Conversor Numérico** com suporte para binário, hexadecimal, octal e decimal
- **Operações Lógicas** (AND, OR, XOR) para trabalhar com valores booleanos
- **Autenticação Segura** com validação de email temporário
- **Sistema de Notificações** por email com OAuth2 do Google
- **Interface Moderna** com Tailwind CSS e efeitos glassmorphism

---

## ⭐ Features

### Autenticação e Usuários
- Registro de usuários com validação forte
- Bloqueio de emails temporários/descartáveis
- Senhas com hash seguro (Django)
- Logout seguro

### Monitoramento do Sistema
- Coleta de métricas em tempo real (CPU, RAM, Disco)
- Análise de desempenho via IA
- Interface de dashboard responsiva

### Conversão Numérica e Lógica Booleana
- Conversão entre bases numéricas (2, 8, 10, 16)
- Operações lógicas booleanas
- Validação de entrada robusta
- Respostas via API

### Notificações
- Emails de boas-vindas para novos usuários
- Notificações de atualização de termos
- Autenticação OAuth2 com Google
- Mensagens coloridas no terminal

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

## 🏗 Arquitetura

### Padrão MVT

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