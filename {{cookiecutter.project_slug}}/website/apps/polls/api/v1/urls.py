from django.urls import path

from .views import list_polls

app_name = "v1"

urlpatterns = [
    path("polls/", list_polls, name="polls"),
]
