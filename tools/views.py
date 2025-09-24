from django.shortcuts import render
from .services.system_metrics import get_system_stats
from .services.ai_analysis import analysis_status
from .services import num_converter
from django.conf import settings
from django.http import JsonResponse
from django.http import HttpResponse
from http import HTTPStatus
from django.contrib.auth.decorators import login_required


if settings.AI_MODE:
    @login_required
    def system_analysis_view(request):
        if request.method == 'GET':
            stats = get_system_stats()
            ai_response = analysis_status()
            return render(request, 'system_analysis.html', {'stats': stats, 'ai': ai_response})
        else:
            return HttpResponse(
                '<h1>Método não permitido<h2>',
                status=HTTPStatus.METHOD_NOT_ALLOWED
            )
else:
    @login_required
    def system_analysis_view(request):
        if request.method == 'GET':
            stats = get_system_stats()
            return render(request, 'system_analysis.html', {'stats': stats})
        else:
            return HttpResponse(
                '<h1>Método não permitido<h1>',
                status=HTTPStatus.METHOD_NOT_ALLOWED
            )


@login_required
def number_converter_page(request):
    if request.method == 'GET':
        return render(request, 'num_converter.html')
    else:
        return HttpResponse(
            '<h1>Método não permitido<h1>',
            status=HTTPStatus.METHOD_NOT_ALLOWED
        )


@login_required
def number_converter_api(request):
    if request.method == 'GET':
        type = request.GET.get('type')
        value = request.GET.get('value')

        match(type):
            case 'bin2dec':
                result = num_converter.bin_to_dec(value)
            case 'dec2bin':
                result = num_converter.dec_to_bin(int(value))
            case 'dec2hex':
                result = num_converter.dec_to_hex(int(value))
            case 'dec2oct':
                result = num_converter.dec_to_oct(int(value))
            case 'hex2dec':
                result = num_converter.hex_to_dec(value)
            case 'oct2dec':
                result = num_converter.oct_to_dec(value)
            case 'and':
                value1 = int(request.GET.get('value1'))
                value2 = int(request.GET.get('value2'))
                result = value1 & value2
            case 'or':
                value1 = int(request.GET.get('value1'))
                value2 = int(request.GET.get('value2'))
                result = value1 | value2
            case 'xor':
                value1 = int(request.GET.get('value1'))
                value2 = int(request.GET.get('value2'))
                result = value1 ^ value2

        return JsonResponse({'result': result})
    else:
        return HttpResponse(
            '<h1>Método não permitido<h1>',
            status=HTTPStatus.METHOD_NOT_ALLOWED
        )
