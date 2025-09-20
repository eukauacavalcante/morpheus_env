from django.shortcuts import render
from django.http import HttpResponse
from http import HTTPStatus
from django.contrib.auth.decorators import login_required


@login_required
def main_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        return HttpResponse(
            '<h1>Método não permitido<h1>',
            status=HTTPStatus.METHOD_NOT_ALLOWED
        )
