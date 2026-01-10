from django.urls import path

from .views import CheckHealthView

app_name = "v1"

urlpatterns = [
    path("health/", CheckHealthView.as_view(), name="health"),
]
