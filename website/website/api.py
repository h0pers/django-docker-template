from django.urls import include, path

app_name = "api"

urlpatterns = [
    path("", include("apps.core.api.urls")),
    path("", include("apps.polls.api.urls")),
]
