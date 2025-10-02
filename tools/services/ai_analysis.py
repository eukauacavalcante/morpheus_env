from groq import Groq
from .system_metrics import get_system_stats
from django.conf import settings


client = Groq(api_key=settings.API_KEY)


def get_analysis():
    status = get_system_stats()
    response = client.chat.completions.create(
        model=settings.AI_MODEL,
        messages=[
            {'role': 'system', 'content': 'Você é um assistente especializado em analisar dados de desempenho do sistema (CPU, RAM e Memória de armazenamento). Sempre se comunique diretamente com o usuário, de forma clara, simples e em apenas um parágrafo. Não mencione valores exatos de uso de CPU ou RAM, pois variam em tempo real e podem confundir. Explique apenas se o nível está baixo, moderado ou alto, destacando os impactos no desempenho. Caso CPU esteja acima de 90% ou RAM acima de 85%, emita um alerta imediato, explicando riscos como lentidão ou travamentos e sugerindo ações preventivas. Para a Memória de armazenamento (HD/SSD), os valores podem ser citados, já que são estáveis. Evite exageros, seja objetivo e sempre forneça orientações práticas. Não utilize negrito. Retorne tudo em apenas um parágrafo.'},
            {'role': 'user', 'content': f'Atual situação do hardware: {status}'}
        ]
    )
    return response.choices[0].message.content
