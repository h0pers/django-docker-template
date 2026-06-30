# Django + Docker ❤️

## Local Development

### Debug (hot reload, mounts source)

```bash
docker compose -f docker-compose.debug.yml up --build
```

Backend available at `http://localhost`.

### Tests

```bash
# Build test image first (only needed when deps change)
docker build --target development -t backend:test .

# Run full test suite
docker compose -f docker-compose.test.yml run --rm test

# Run specific test file
docker compose -f docker-compose.test.yml run --rm test pytest apps/core/tests/test_something.py

# Run with coverage
docker compose -f docker-compose.test.yml run --rm test ./pytest.sh --ci
```

### Production (local smoke test)

```bash
# Uses pre-built image from GHCR - does not build locally
docker compose up
```

---

## VPS First-Time Setup

Before the first deploy, run these commands on the VPS to register the systemd service. This is a one-time manual step — the deploy workflow does not handle it.

```bash
REPO_NAME="$REPO_NAME"
DEPLOY_USER=$VPS_USER   # the user set in VPS_USER GitHub secret
APP_DIR="/home/$DEPLOY_USER/$REPO_NAME"

sudo tee /etc/systemd/system/$REPO_NAME.service <<SERVICE
[Unit]
Description=$REPO_NAME
After=docker.service network-online.target
Requires=docker.service

[Service]
Type=oneshot
RemainAfterExit=yes
WorkingDirectory=$APP_DIR
ExecStart=/usr/bin/docker compose up -d
ExecStop=/usr/bin/docker compose down
TimeoutStartSec=300

[Install]
WantedBy=multi-user.target
SERVICE

sudo systemctl daemon-reload
sudo systemctl enable $REPO_NAME.service
```

After this, all subsequent deploys are handled automatically by the GitHub Actions workflow on every push to `master`.

## Per-Server Runtime Configuration

`GUNICORN_WORKERS` and `GUNICORN_TIMEOUT` are not deployed by CI - they are server-specific (depends on CPU/memory). Configure them once by creating `docker-compose.override.yml` on the server. Docker Compose merges it automatically and CI never overwrites it.

```yaml
services:
  backend:
    environment:
      - "GUNICORN_WORKERS=4"
      - "GUNICORN_TIMEOUT=60"
```

Adjust `GUNICORN_WORKERS` to `(2 * CPU cores) + 1`. If the file is absent, defaults (`2` workers, `60`s timeout) apply.
