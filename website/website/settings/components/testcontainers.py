TESTCONTAINERS = {
    "postgres": {
        "image": "postgres:17-alpine",
    },
}

TEST_RUNNER = "django_testcontainers_plus.runner.TestcontainersRunner"
