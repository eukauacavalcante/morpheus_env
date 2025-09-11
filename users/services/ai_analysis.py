from groq import Groq
from .system_metrics import get_system_stats
from django.conf import settings


client = Groq(api_key=settings.API_KEY)

def analysis_status():
    status = get_system_stats()
    response = client.chat.completions.create(
        model=settings.AI_MODEL,
        messages=[
            {'role': 'system', 'content': 'Você é um assistente que analisa dados sobre a CPU, RAM e o SSD do usuário. Retorne explicando os dados em uso e os possíveis motivos. Dados com porcentagens altas (exemplo: CPU em 90%), retorne um aviso ao usuário e explique o que deve ser feito para previnir problemas. Seja direto, de forma resumida. Não utilize negrito. Retorne apenas um parágrafo.'},
            {'role': 'user', 'content': f'Atual situação do hardware do usuário: {status}'}
        ]
    )
    return response.choices[0].message.content
