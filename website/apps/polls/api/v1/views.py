from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.polls.api.v1.schema import check_health_schema


class CheckHealthView(APIView):
    @check_health_schema
    def get(self, request):
        return Response(status=status.HTTP_200_OK)
