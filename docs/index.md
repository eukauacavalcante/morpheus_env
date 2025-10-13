# Morpheus Env - Documentação Completa

Bem-vindo à documentação do **Morpheus Env**, um simulador web educacional para análise de sistemas computacionais com suporte a IA.

## 📚 Índice

### Começar

- [Visão Geral](./overview.md) - O que é Morpheus Env
- [Pré-requisitos](./prerequisites.md) - Requisitos de sistema
- [Instalação](./installation.md) - Setup completo
- [Configuração](./configuration.md) - Variáveis de ambiente

### Desenvolvimento

- [Development](./development.md) - Workflow local
- [Guidelines](./guidelines.md) - Padrões de código do projeto
- [Contributing](./contributing.md) - Como contribuir

### Referência

- [Architecture](./architecture.md) - Design técnico
- [Project Structure](./project-structure.md) - Organização de arquivos
- [Authentication](./authentication.md) - Sistema de autenticação
- [Security](./security.md) - Proteções implementadas
- [API Reference](./api-reference.md) - Endpoints disponíveis
- [Tools](./tools.md) - Dependências do projeto

### Manutenção

- [Release Notes](./release-notes.md) - Histórico de versões

---

## 🎯 Visão Rápida

**Morpheus Env** é um simulador educacional que oferece:

- Monitoramento em tempo real de sistema (CPU, RAM, Disco)
- Análise inteligente com IA (Groq AI)
- Conversor numérico (binário, hexadecimal, octal, decimal)
- Operações lógicas booleanas (AND, OR, XOR)
- Autenticação segura com validação de email
- Notificações por email com OAuth2 Google

**Stack:** Python 3.12 • Django 5.2 • SQLite • Tailwind CSS • Groq AI

---

## 🚀 Quick Start

```bash
# Clonar repositório
git clone https://github.com/eukauacavalcante/morpheus_env.git
cd morpheus_env

# Criar ambiente virtual
python -m venv venv
source venv/bin/activate  # ou `venv\Scripts\activate` no Windows

# Instalar dependências
pip install -r requirements.txt

# Configurar variáveis de ambiente
cp .env.example .env
# Edite o arquivo .env com suas configurações

# Executar migrações
python manage.py migrate

# Criar superusuário
python manage.py createsuperuser

# Iniciar servidor
python manage.py runserver
```

Acesse: `http://localhost:8000`

---

## ⚠️ Avisos Importantes

- **Projeto Acadêmico**: Este é um projeto experimental para fins educacionais
- **Não use em produção** sem adaptações de segurança específicas
- Os resultados não devem ser interpretados como análises profissionais
- Sempre configure variáveis de ambiente sensíveis de forma segura

---

## 📞 Suporte e Contato

- Email: [morpheusenv@gmail.com](mailto:morpheusenv@gmail.com)
- GitHub: [eukauacavalcante/morpheus_env](https://github.com/eukauacavalcante/morpheus_env)
- LinkedIn Desenvolvedor: [Kauã Cavalcante](https://www.linkedin.com/in/eukauacavalcante)

---

## 📄 Licença

Este projeto está licenciado sob a **GNU GENERAL PUBLIC LICENSE** - veja o arquivo [LICENSE](https://github.com/eukauacavalcante/morpheus_env/blob/main/LICENSE) para detalhes.

---

## Próximas Etapas

Para começar a trabalhar com o projeto, consulte:

- [Visão Geral](./overview.md) - Entenda o que é o Morpheus Env
- [Pré-requisitos](./prerequisites.md) - Requisitos do sistema
- [Instalação](./installation.md) - Como configurar o ambiente
- [Configuração](./development.md) - Comece a desenvolver

**Desenvolvido com carinho para educação e experimentação :)**

<div align="center">
    © 2025 - Morpheus Env - Projeto Acadêmico e Experimental
</div>
