from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.polls.api.v1.schema import list_polls_schema
from apps.polls.api.v1.serializers import PollSerializer

FAKE_POLLS = [
    {"id": 1, "question": "What is your favorite color?"},
    {"id": 2, "question": "What is your favorite food?"},
]


@list_polls_schema
@api_view(["GET"])
def list_polls(request):
    serializer = PollSerializer(FAKE_POLLS, many=True)
    return Response(serializer.data)
