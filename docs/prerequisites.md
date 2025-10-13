# Pré-requisitos do Projeto

Requisitos de sistema e conhecimentos necessários para trabalhar com o Morpheus Env.

---

## Requisitos de Sistema

### Processador

- **Mínimo**: Dual-core 1.5GHz
- **Recomendado**: Quad-core 2.0GHz+

### Memória (RAM)

| Cenário | RAM |
|---------|-----|
| Desenvolvimento | 4GB |
| Desenvolvimento + IA | 8GB |
| Produção | 16GB+ |

Verificar disponível:

```bash
# Linux/macOS
free -h

# Windows
wmic os get TotalVisibleMemorySize
```

### Armazenamento

- Código-fonte: ~50MB
- Virtual environment: ~500MB
- Banco de dados (dev): ~10MB
- **Total mínimo**: ~600MB

---

## Software Obrigatório

### Python 3.12+

**Verificar instalação**:

```bash
python --version  # Deve retornar 3.12+
```

**Download**: [python.org](https://www.python.org/downloads/)

### pip (Gerenciador de Pacotes)

Incluído com Python 3.4+

```bash
pip --version
```

### Git

Para versionamento e contribuição.

**Download**: [git-scm.com](https://git-scm.com)

```bash
git --version
```

### Navegador Web (Moderno)

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

---

## Conhecimento Prévio

Você deve estar confortável com:

- **Python básico**: sintaxe, loops, condicionais, funções
- **Django**: Models, Views, Templates, ORM
- **HTML/CSS**: estrutura básica, seletores
- **JavaScript**: variáveis, funções, async/await
- **Git**: clone, commit, push, branches

Se não tiver experiência, consulte:

- [Real Python](https://realpython.com)
- [Django Documentation](https://docs.djangoproject.com)

---

## APIs Externas (Opcionais para Dev)

### Groq AI

Para usar análise inteligente:

- Conta em [console.groq.com](https://console.groq.com)
- API key gratuita

### Google OAuth2

Para envio de emails:

- Projeto em [Google Cloud Console](https://console.cloud.google.com)
- Credenciais OAuth2

---

## Próximas Etapas

- [Instalação](./installation.md) - Setup completo
- [Configuração](./configuration.md) - Variáveis de ambiente
