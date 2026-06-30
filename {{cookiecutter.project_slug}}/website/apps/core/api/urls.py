from django.urls import path

from apps.core.api.views import health

app_name = "core"

urlpatterns = [
    path("health/", health, name="health"),
]
