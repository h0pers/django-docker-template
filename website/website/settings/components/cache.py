"""Cache configuration settings (Redis)."""

from website.settings import env

CACHES = {
    "default": {
        **env.cache(),
        "BACKEND": "django_redis.cache.RedisCache",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}
