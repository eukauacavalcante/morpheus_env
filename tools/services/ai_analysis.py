from groq import Groq
from .system_metrics import get_system_stats
from django.conf import settings


client = Groq(api_key=settings.API_KEY)


def analysis_status():
    status = get_system_stats()
    response = client.chat.completions.create(
        model=settings.AI_MODEL,
        messages=[
            {'role': 'system', 'content': 'Você é um assistente que analisa os dados de uso de CPU, RAM e SSD. Sempre fale diretamente com o usuário, explicando de forma clara e resumida o que cada porcentagem de uso significa. Quando algum dado estiver em nível alto (ex.: CPU acima de 90%, RAM acima de 85% ou SSD acima de 90%), dê um aviso imediato e explique os riscos e o que deve ser feito para prevenir travamentos ou lentidão. Seja objetivo, use apenas um parágrafo e não utilize negrito.'},
            {'role': 'user', 'content': f'Atual situação do hardware: {status}'}
        ]
    )
    return response.choices[0].message.content
