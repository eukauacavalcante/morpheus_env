from django.shortcuts import render
from .services.system_metrics import get_system_stats
from .services.ai_analysis import analysis_status


def system_dashboard(request):
    stats = get_system_stats()
    ai_response = analysis_status()
    return render(request, 'system_analysis.html', {'stats':stats, 'ai':ai_response})
