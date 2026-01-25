TESTCONTAINERS = {
    "postgres": {
        "image": "postgres:17",
    },
}

TEST_RUNNER = "django_testcontainers_plus.runner.TestcontainersRunner"
