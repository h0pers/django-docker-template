"""
Security-related settings (shared across environments).

Note: SESSION_COOKIE_SECURE, CSRF_COOKIE_SECURE, SECURE_SSL_REDIRECT,
and SECURE_HSTS_SECONDS are configured per-environment.
"""

from website.settings import env

# CSRF settings
CSRF_TRUSTED_ORIGINS = env.list("DJANGO_CSRF_TRUSTED_ORIGINS", default=[])
# Proxy header for SSL detection behind reverse proxy
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
