from django.urls import include, path

app_name = "api"

urlpatterns = [
    path("", include("apps.core.api.urls")),
{%- if cookiecutter.use_drf == "y" %}
    path("", include("apps.polls.api.urls")),
{%- endif %}
]
