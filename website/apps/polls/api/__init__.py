from django.urls import path, include

app_name = "polls"

urlpatterns = [
    path("v1/", include("apps.polls.api.v1.urls")),
]
