from django.shortcuts import render
from .services.system_metrics import get_system_stats
from .services.ai_analysis import analysis_status
from .services.num_converter import bin_to_dec, dec_to_bin, dec_to_hex, dec_to_oct, hex_to_dec, oct_to_dec
from django.conf import settings
from django.http import JsonResponse


if settings.AI_MODE:
    def system_analysis_view(request):
        stats = get_system_stats()
        ai_response = analysis_status()
        return render(request, 'system_analysis.html', {'stats': stats, 'ai': ai_response})
else:
    def system_analysis_view(request):
        stats = get_system_stats()
        return render(request, 'system_analysis.html', {'stats': stats})


def number_converter_page(request):
    return render(request, 'num_converter.html')


def number_converter_api(request):
    type = request.GET.get('type')
    value = request.GET.get('value')

    match(type):
        case 'bin2dec':
            result = bin_to_dec(value)
        case 'dec2bin':
            result = dec_to_bin(int(value))
        case 'dec2hex':
            result = dec_to_hex(int(value))
        case 'dec2oct':
            result = dec_to_oct(int(value))
        case 'hex2dec':
            result = hex_to_dec(value)
        case 'oct2dec':
            result = oct_to_dec(value)

    return JsonResponse({'result': result})
