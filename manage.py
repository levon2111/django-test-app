#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

import dotenv
import environ


def main():
    """Run administrative tasks."""
    ROOT_DIR = (
            environ.Path(__file__) - 1
    )
    env = environ.Env()
    environment = env("SETTINGS") if "SETTINGS" in os.environ else 'local'
    env_file = f".envs/.{environment}/.django"
    dotenv.read_dotenv(str(ROOT_DIR.path(env_file)))
    settings = os.environ.get('SETTINGS', 'local')

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'help_gamblers.settings.{settings}')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
