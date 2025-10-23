# Referência de API

Endpoints REST do Morpheus Env.

---

## Autenticação

Todos os endpoints suportam dois métodos de autenticação:

1. **Sessão Django** (tradicional)
2. **JWT (JSON Web Token)** - Recomendado para aplicações modernas

Se não autenticado: `HTTP 401 Unauthorized`

### Obtendo um Token JWT
```bash
curl -X POST http://localhost:8000/accounts/api/v1/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "usuario", "password": "senha123"}'
```

**Response (200)**:
```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

**Usando o Token** - Adicione o header `Authorization`:
```bash
curl -H "Authorization: Bearer {access_token}" \
  http://localhost:8000/sistema/monitoramento/api/v1/metrics
```

**Refresh Token** (válido por 1 dia):
```bash
curl -X POST http://localhost:8000/accounts/api/v1/token/refresh/ \
  -H "Content-Type: application/json" \
  -d '{"refresh": "{refresh_token}"}'
```

- **Access Token**: Válido por 10 minutos
- **Refresh Token**: Válido por 1 dia

---

## Endpoints

### GET /sistema/monitoramento/api/v1/metrics

Retorna métricas atuais do sistema.

**Rate Limit**: 20 requisições/minuto

**Response (200)**:

```json
{
  "data": {
    "cpu_percent": 45.2,
    "ram_percent": 62.5,
    "ram_total": 16.0,
    "ram_used": 10.0,
    "memory_used": 450.5,
    "memory_total": 1000.0
  }
}
```

**Campos**:

- `cpu_percent` (float): 0-100
- `ram_percent` (float): 0-100
- `ram_total` (float): GB
- `ram_used` (float): GB
- `memory_used` (float): GB (disco)
- `memory_total` (float): GB (disco)

**Exemplo**:

```bash
curl -b "sessionid=abc123" \
  http://localhost:8000/sistema/monitoramento/api/v1/metrics
```

```javascript
const response = await fetch('/sistema/monitoramento/api/v1/metrics');
const data = await response.json();
console.log(`CPU: ${data.data.cpu_percent}%`);
```

---

### GET /sistema/monitoramento/api/v1/ai

Análise inteligente das métricas.

**Rate Limit**: 10 requisições/minuto

**Response (200) - Com IA ativada**:

```json
{
  "ai": "O sistema está operando normalmente. CPU em 45%, RAM em 62% com 10GB de 16GB em uso..."
}
```

**Response (200) - Sem IA**:

```json
{
  "ai": "<p class=\"text-xl text-red-500\">Análise por IA indisponível no momento :(<br>...</p>"
}
```

**Notas**:

- IA disponível se `AI_MODE=True` e API key válida
- Pode levar 2-5 segundos

---

### GET /sistema/conversor/api/v1/converter

Converte números entre bases.

**Parâmetros**:

- `type` (string): Tipo de conversão
- `value` (string): Valor a converter

**Tipos de conversão**:

- `bin2dec` - Binário → Decimal
- `dec2bin` - Decimal → Binário
- `hex2dec` - Hexadecimal → Decimal
- `dec2hex` - Decimal → Hexadecimal
- `oct2dec` - Octal → Decimal
- `dec2oct` - Decimal → Octal

**Response (200)**:

```json
{
  "result": 10
}
```

**Response (400)**:

```json
{
  "result": "Error ao calcular"
}
```

**Exemplos**:

```bash
# Binário para Decimal
curl "http://localhost:8000/sistema/conversor/api/v1/converter?type=bin2dec&value=1010"
# Retorna: 10

# Decimal para Hexadecimal
curl "http://localhost:8000/sistema/conversor/api/v1/converter?type=dec2hex&value=255"
# Retorna: FF
```

---

### GET /sistema/conversor/api/v1/converter (Operações Lógicas)

Operações AND, OR, XOR.

**Parâmetros**:

- `type` (string): `and`, `or`, `xor`
- `value1` (string): 0 ou 1
- `value2` (string): 0 ou 1

**Response (200)**:

```json
{
  "result": 1
}
```

**Tabelas de Verdade**:

| A | B | AND | OR | XOR |
|---|---|-----|----|----|
| 0 | 0 | 0   | 0  | 0  |
| 0 | 1 | 0   | 1  | 1  |
| 1 | 0 | 0   | 1  | 1  |
| 1 | 1 | 1   | 1  | 0  |

**Exemplos**:

```bash
curl "http://localhost:8000/sistema/conversor/api/v1/converter?type=and&value1=1&value2=1"
# Retorna: 1

curl "http://localhost:8000/sistema/conversor/api/v1/converter?type=xor&value1=1&value2=0"
# Retorna: 1
```

---

## Status HTTP

| Código | Significado |
|--------|------------|
| 200 | OK |
| 302 | Redirect (sessão Django - deprecado) |
| 400 | Entrada inválida |
| 401 | Não autenticado / Token JWT inválido |
| 429 | Rate limit excedido |
| 500 | Erro no servidor |

---

## Rate Limiting

Exceder limite retorna:

```
HTTP 429 Too Many Requests
```

**Limites atuais**:

| Endpoint | Limite |
|----------|--------|
| `/sistema/monitoramento/api/v1/metrics` | 20/minuto |
| `/sistema/monitoramento/api/v1/ai` | 10/minuto |
| `/sistema/conversor/api/v1/converter` | Ilimitado |

---

## Exemplos Completos

### Python + Requests

```python
import requests

# Obter tokens
auth_response = requests.post(
    'http://localhost:8000/accounts/api/v1/token/',
    json={'username': 'usuario', 'password': 'senha123'}
)
access_token = auth_response.json()['access']

# Headers com JWT
headers = {'Authorization': f'Bearer {access_token}'}

# Métricas
r = requests.get(
    'http://localhost:8000/sistema/monitoramento/api/v1/metrics',
    headers=headers
)
print(f"CPU: {r.json()['data']['cpu_percent']}%")
```

### JavaScript + Fetch

```javascript
async function getMetrics() {
    const response = await fetch('/sistema/monitoramento/api/v1/metrics');
    const data = await response.json();
    console.log(`CPU: ${data.data.cpu_percent}%`);
}

async function convertNumber(type, value) {
    const url = `/sistema/conversor/v1/api?type=${type}&value=${value}`;
    const response = await fetch(url);
    const data = await response.json();
    return data.result;
}

// Uso
(async () => {
    await getMetrics();
    const result = await convertNumber('dec2bin', '10');
    console.log('10 em binário:', result);
})();
```

---

## Próximas Etapas

- [Segurança](./security.md) - Proteções implementadas
- [Desenvolvimento](./development.md) - Como testar APIs localmente
