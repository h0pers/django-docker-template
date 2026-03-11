from django.conf import settings


def test_django_mode_is_test():
    assert settings.DJANGO_ENV == "test"
