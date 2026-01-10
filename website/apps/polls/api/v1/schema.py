from drf_spectacular.utils import OpenApiResponse, extend_schema
from rest_framework import status

from apps.polls.api.v1 import docstring

check_health_schema = extend_schema(
    summary="Check Health API",
    description=docstring.CHECK_HEALTH_DOCS,
    responses={
        status.HTTP_200_OK: OpenApiResponse(
            description=docstring.CHECK_HEALTH_RESPONSE_DOCS,
        ),
    },
)
