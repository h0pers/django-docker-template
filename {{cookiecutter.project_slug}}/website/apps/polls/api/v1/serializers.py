from rest_framework import serializers


class PollSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    question = serializers.CharField()
