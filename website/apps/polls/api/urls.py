from django.urls import include, path

app_name = "polls"

urlpatterns = [
    path("v1/", include("apps.polls.api.v1.urls")),
]
