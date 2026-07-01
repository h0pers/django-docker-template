{%- if cookiecutter.use_drf == "y" -%}
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.core.api.schema import health_schema


@health_schema
@api_view(["GET"])
def health(request) -> Response:
    return Response({"status": "ok"})
{% else -%}
from django.http import JsonResponse


def health(request) -> JsonResponse:
    return JsonResponse({"status": "ok"})
{% endif -%}
