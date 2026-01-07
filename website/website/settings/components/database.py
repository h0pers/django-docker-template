"""
Database configuration settings.
"""

from pathlib import Path

from website.settings import env

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": Path(env.str("DJANGO_SQLITE_DIR", default=".")) / "db.sqlite3",
    }
}

# If POSTGRES_DB is set, use PostgreSQL
if env.str("POSTGRES_DB", default=""):
    DATABASES["default"] = {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("POSTGRES_DB"),
        "USER": env("POSTGRES_USER"),
        "PASSWORD": env("POSTGRES_PASSWORD"),
        "HOST": env("POSTGRES_HOST"),
        "PORT": env("POSTGRES_PORT"),
    }
