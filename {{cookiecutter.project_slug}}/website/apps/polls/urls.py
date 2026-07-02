from django.urls import path

from .views import spa_view

app_name = "polls"

urlpatterns = [
    path("", spa_view, name="spa"),
    path("<path:path>", spa_view, name="spa-path"),
]
