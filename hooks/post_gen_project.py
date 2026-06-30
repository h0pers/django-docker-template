import shutil
from pathlib import Path

USE_DRF = "{{ cookiecutter.use_drf }}" == "y"

REMOVE_PATHS_NO_DRF = [
    "website/apps/polls",
    "website/website/settings/components/rest_framework.py",
    "website/website/settings/components/cors.py",
    "website/apps/core/api/schema.py",
    "website/apps/core/api/docstring.py",
]


def remove_paths(paths: list[str]) -> None:
    for path_str in paths:
        path = Path(path_str)
        if path.is_dir():
            shutil.rmtree(path)
        elif path.is_file():
            path.unlink()


def main() -> None:
    if not USE_DRF:
        remove_paths(REMOVE_PATHS_NO_DRF)


if __name__ == "__main__":
    main()