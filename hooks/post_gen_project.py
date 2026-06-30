import shutil
import subprocess
from pathlib import Path

USE_DRF = "{{ cookiecutter.use_drf }}" == "y"
USE_WAGTAIL = "{{ cookiecutter.use_wagtail }}" == "y"

REMOVE_PATHS_NO_DRF = [
    "website/apps/polls",
    "website/website/settings/components/rest_framework.py",
    "website/website/settings/components/cors.py",
    "website/apps/core/api/schema.py",
    "website/apps/core/api/docstring.py",
]

REMOVE_PATHS_NO_WAGTAIL = [
    "website/apps/cms",
    "website/website/settings/components/wagtail.py",
]


def remove_paths(paths: list[str]) -> None:
    for path_str in paths:
        path = Path(path_str)
        if path.is_dir():
            shutil.rmtree(path)
        elif path.is_file():
            path.unlink()


def generate_lock_file() -> None:
    try:
        subprocess.run(["uv", "lock"], check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("WARNING: Could not run 'uv lock'. Run it manually to generate uv.lock.")


def main() -> None:
    if not USE_DRF:
        remove_paths(REMOVE_PATHS_NO_DRF)

    if not USE_WAGTAIL:
        remove_paths(REMOVE_PATHS_NO_WAGTAIL)

    generate_lock_file()


if __name__ == "__main__":
    main()