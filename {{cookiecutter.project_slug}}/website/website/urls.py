"""
URL configuration for project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
{%- if cookiecutter.use_vue == "y" %}
from django.views.generic import RedirectView
{%- endif %}
{%- if cookiecutter.use_drf == "y" %}
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
{%- endif %}
{%- if cookiecutter.use_wagtail == "y" %}
from wagtail import urls as wagtail_urls
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
{%- endif %}

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("website.api")),
{%- if cookiecutter.use_wagtail == "y" %}
    path("cms/", include(wagtailadmin_urls)),
    path("documents/", include(wagtaildocs_urls)),
{%- endif %}
]
{%- if cookiecutter.use_drf == "y" %}

if settings.DEBUG:
    urlpatterns += [
        path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
        path(
            "api/docs/",
            SpectacularSwaggerView.as_view(url_name="schema"),
            name="swagger-ui",
        ),
    ]
{%- endif %}

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
{%- if cookiecutter.use_vue == "y" %}

urlpatterns += [
    path("", RedirectView.as_view(pattern_name="polls:spa")),
    path("app/", include("apps.polls.urls")),
]
{%- endif %}
{%- if cookiecutter.use_wagtail == "y" %}

urlpatterns += [
    path("", include(wagtail_urls)),
]
{%- endif %}
