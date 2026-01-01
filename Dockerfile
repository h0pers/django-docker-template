FROM ghcr.io/astral-sh/uv:python3.11-alpine AS base

# uv options
ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_PROJECT_ENVIRONMENT=/opt/venv \
    VIRTUAL_ENV=/opt/venv \
    PATH="/opt/venv/bin:$PATH"

FROM base AS deps

ARG PROJECT_NAME=website
ARG DJANGO_BASE_DIR=/usr/src/$PROJECT_NAME
WORKDIR $DJANGO_BASE_DIR

RUN apk --no-cache add python3-dev libpq-dev

COPY pyproject.toml uv.lock ./

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-install-project --no-dev

FROM base

ARG USER=user
ARG USER_UID=1001
ARG PROJECT_NAME=website
ARG GUNICORN_PORT=8000
ARG GUNICORN_WORKERS=2
# the value is in seconds
ARG GUNICORN_TIMEOUT=60
ARG GUNICORN_LOG_LEVEL=info
ARG DJANGO_BASE_DIR=/usr/src/$PROJECT_NAME
ARG DJANGO_STATIC_ROOT=/var/www/static
ARG DJANGO_MEDIA_ROOT=/var/www/media
ARG DJANGO_SQLITE_DIR=/sqlite
# The superuser with the data below will be created only if there are no users in the database!
ARG DJANGO_SUPERUSER_USERNAME=admin
ARG DJANGO_SUPERUSER_PASSWORD=admin
ARG DJANGO_SUPERUSER_EMAIL=admin@example.com
ARG DJANGO_DEV_SERVER_PORT=8000

ENV \
    USER=$USER \
    USER_UID=$USER_UID \
    PROJECT_NAME=$PROJECT_NAME \
    GUNICORN_PORT=$GUNICORN_PORT \
    GUNICORN_WORKERS=$GUNICORN_WORKERS \
    GUNICORN_TIMEOUT=$GUNICORN_TIMEOUT \
    GUNICORN_LOG_LEVEL=$GUNICORN_LOG_LEVEL \
    DJANGO_BASE_DIR=$DJANGO_BASE_DIR \
    DJANGO_STATIC_ROOT=$DJANGO_STATIC_ROOT \
    DJANGO_MEDIA_ROOT=$DJANGO_MEDIA_ROOT \
    DJANGO_SQLITE_DIR=$DJANGO_SQLITE_DIR \
    DJANGO_SUPERUSER_USERNAME=$DJANGO_SUPERUSER_USERNAME \
    DJANGO_SUPERUSER_PASSWORD=$DJANGO_SUPERUSER_PASSWORD \
    DJANGO_SUPERUSER_EMAIL=$DJANGO_SUPERUSER_EMAIL \
    DJANGO_DEV_SERVER_PORT=$DJANGO_DEV_SERVER_PORT

# Runtime deps only + user
RUN apk add --no-cache su-exec libpq-dev && \
    adduser -s /bin/sh -D -u $USER_UID $USER

COPY --from=deps /opt/venv /opt/venv

WORKDIR $DJANGO_BASE_DIR

COPY docker-entrypoint.sh /
COPY docker-cmd.sh /
COPY $PROJECT_NAME $DJANGO_BASE_DIR

RUN chmod +x /docker-entrypoint.sh /docker-cmd.sh && \
    mkdir -p $DJANGO_STATIC_ROOT $DJANGO_MEDIA_ROOT $DJANGO_SQLITE_DIR && \
    chown -R $USER:$USER $DJANGO_BASE_DIR $DJANGO_STATIC_ROOT $DJANGO_MEDIA_ROOT $DJANGO_SQLITE_DIR

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["/docker-cmd.sh"]

EXPOSE $GUNICORN_PORT
