from django.http import HttpResponse
from django.shortcuts import render


def spa_view(request, **kwargs) -> HttpResponse:
    return render(request, template_name="polls/app.html", context={})
