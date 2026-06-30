"""
Wagtail CMS settings.
"""

from website.settings import env

WAGTAIL_SITE_NAME = env.str("WAGTAIL_SITE_NAME", default="{{ cookiecutter.project_name }}")

WAGTAILADMIN_BASE_URL = env.str("WAGTAILADMIN_BASE_URL", default="http://localhost")

WAGTAILDOCS_EXTENSIONS = [
    "csv",
    "docx",
    "key",
    "odt",
    "pdf",
    "pptx",
    "rtf",
    "txt",
    "xlsx",
    "zip",
]

DATA_UPLOAD_MAX_NUMBER_FIELDS = 10_000