"""
Database configuration settings.
"""

import os

from website.settings import env

if "DATABASE_URL" in os.environ:
    DATABASES = {"default": env.db()}
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": env.str("POSTGRES_DB"),
            "USER": env.str("POSTGRES_USER"),
            "PASSWORD": env.str("POSTGRES_PASSWORD"),
            "HOST": env.str("POSTGRES_HOST"),
            "PORT": env.str("POSTGRES_PORT"),
        }
    }
