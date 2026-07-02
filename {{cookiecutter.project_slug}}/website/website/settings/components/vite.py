"""
Django Vite settings for Vue 3 frontend integration.
"""

from website.settings import BASE_DIR

DJANGO_VITE = {
    "default": {
        "dev_mode": False,
        "static_url_prefix": "dist",
        "manifest_path": BASE_DIR / "static" / "dist" / ".vite" / "manifest.json",
    }
}
