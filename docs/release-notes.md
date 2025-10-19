# Release Notes

Histórico de versões do Morpheus Env.

---

## [1.0.0] - 19/10/2025

### Added

**Funcionalidades Principais**:

- Monitoramento de sistema em tempo real (CPU, RAM, Disco)
- Análise inteligente com Groq AI
- Conversor numérico (binário, octal, decimal, hexadecimal)
- Operações lógicas booleanas (AND, OR, XOR)

**Autenticação e Segurança**:

- Sistema de registro com validações customizadas
- Bloqueio de emails temporários/descartáveis
- Proteção CSRF em formulários
- Hash de senha com PBKDF2 (260k iterações)
- Proteção XSS (auto-escape de templates)

**Notificações**:

- Emails de boas-vindas para novos usuários
- Notificações de atualização de termos
- Autenticação OAuth2 Google

**Interface**:

- Dashboard responsivo com Tailwind CSS
- Efeito glassmorphism na UI
- Bootstrap Icons integrado

**Rate Limiting**:

- 20 requisições/minuto para métricas
- 10 requisições/minuto para análise IA

**Django Axes**:

- 5 tentativas válidas para o login (proteção contra força bruta)

**Documentação Completa**:

- Visão geral do projeto
- Guia de instalação
- Referência de API
- Guia de contribuição

### Tech Stack

**Backend**:

- Python 3.12
- Django 5.2
- SQLite (dev) / PostgreSQL (prod)
- Groq AI
- psutil

**Frontend**:

- Django Templates
- Tailwind CSS 4
- Bootstrap Icons
- JavaScript Vanilla

---

## Suporte de Versões

| Versão | Status | Suporta | Fim de Suporte |
|--------|--------|--------|----------------|
| 1.0.0 | Estável | Python 3.12, Django 5.2 | TBD |

---

## Roadmap Futuro

### Curto Prazo

- API REST com autenticação por token
- Cache de 5 segundos para métricas
- Testes unitários

### Médio Prazo

- Views assíncronas
- Suporte PostgreSQL completo
- Histórico de análises
- Dashboard avançado com gráficos

### Longo Prazo

- Aplicação mobile
- Integração com mais modelos de IA
- Exportação de relatórios

---

## Status Atual

**Projeto Acadêmico e Experimental**

Não recomendado para produção sem adaptações de segurança específicas.

---

## Como Relatar Bugs

Abra uma [Issue](https://github.com/eukauacavalcante/morpheus_env/issues) com:

- Descrição clara do bug
- Passos para reproduzir
- Resultado esperado vs. real
- Environment (SO, Python version, etc)

---

## Como Sugerir Melhorias

Abra uma [Discussion](https://github.com/eukauacavalcante/morpheus_env/discussions) com:

- Descrição da melhoria
- Caso de uso
- Benefícios esperados

---

## Contato

- Email: morpheusenv@gmail.com
- GitHub: [eukauacavalcante/morpheus_env](https://github.com/eukauacavalcante/morpheus_env)
- LinkedIn: [Kauã Cavalcante](https://www.linkedin.com/in/eukauacavalcante)

---

## Licença

GNU GENERAL PUBLIC LICENSE - veja [LICENSE](https://github.com/eukauacavalcante/morpheus_env/blob/main/LICENSE)
