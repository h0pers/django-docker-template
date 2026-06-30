FROM ghcr.io/astral-sh/uv:python3.11-alpine AS base

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_PROJECT_ENVIRONMENT=/opt/venv \
    VIRTUAL_ENV=/opt/venv \
    PATH="/opt/venv/bin:$PATH"

FROM base AS deps-base

RUN apk --no-cache add python3-dev libpq-dev

COPY pyproject.toml uv.lock ./

FROM deps-base AS deps

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-install-project --no-dev

FROM deps-base AS deps-dev

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-install-project

FROM base AS runtime

ENV USER=user \
    USER_UID=1001 \
    PROJECT_NAME=website \
    DJANGO_BASE_DIR=/usr/src/website \
    GUNICORN_PORT=8000 \
    GUNICORN_LOG_LEVEL=info \
    DJANGO_STATIC_ROOT=/var/www/static \
    DJANGO_MEDIA_ROOT=/var/www/media

RUN apk add --no-cache su-exec libpq-dev && \
    adduser -s /bin/sh -D -u $USER_UID $USER

WORKDIR $DJANGO_BASE_DIR

COPY docker-cmd.sh /
COPY $PROJECT_NAME $DJANGO_BASE_DIR

RUN chmod +x /docker-cmd.sh && \
    mkdir -p $DJANGO_STATIC_ROOT $DJANGO_MEDIA_ROOT && \
    chown -R $USER:$USER $DJANGO_BASE_DIR $DJANGO_STATIC_ROOT $DJANGO_MEDIA_ROOT

CMD ["/docker-cmd.sh"]

EXPOSE $GUNICORN_PORT

FROM runtime AS development

COPY --from=deps-dev /opt/venv /opt/venv

FROM runtime AS production

COPY --from=deps /opt/venv /opt/venv
