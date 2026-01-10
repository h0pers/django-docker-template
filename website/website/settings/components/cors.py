"""
Cors Headers settings.
"""

from corsheaders.defaults import default_headers, default_methods

from website.settings import env

CORS_ALLOWED_ORIGINS = env.list("CORS_ALLOWED_ORIGINS", default=[])
CORS_ALLOW_METHODS = env.list("CORS_ALLOW_METHODS", default=default_methods)
CORS_ALLOW_HEADERS = env.list("CORS_ALLOW_HEADERS", default=default_headers)
