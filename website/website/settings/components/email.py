"""
Email configuration settings.
"""

from website.settings import env

# Email settings
EMAIL_HOST = env.str("DJANGO_EMAIL_HOST", default="localhost")
EMAIL_PORT = env.int("DJANGO_EMAIL_PORT", default=25)
EMAIL_HOST_USER = env.str("DJANGO_EMAIL_HOST_USER", default="")
EMAIL_HOST_PASSWORD = env.str("DJANGO_EMAIL_HOST_PASSWORD", default="")
EMAIL_USE_TLS = env.bool("DJANGO_EMAIL_USE_TLS", default=False)

# Email address that error messages come from.
SERVER_EMAIL = env.str("DJANGO_SERVER_EMAIL", default="root@localhost")

# Default email address to use for various automated correspondence from the site managers.
DEFAULT_FROM_EMAIL = env.str("DJANGO_DEFAULT_FROM_EMAIL", default="webmaster@localhost")

# People who get code error notifications.
ADMIN_NAME = env.str("DJANGO_ADMIN_NAME", default="")
ADMIN_EMAIL = env.str("DJANGO_ADMIN_EMAIL", default="")

if ADMIN_EMAIL:
    ADMINS = [(ADMIN_NAME, ADMIN_EMAIL)]
