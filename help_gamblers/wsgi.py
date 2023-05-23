"""
WSGI config for help_gamblers project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

import dotenv
import environ
from django.core.wsgi import get_wsgi_application

ROOT_DIR = (
        environ.Path(__file__) - 2
)

env = environ.Env()
environment = env("SETTINGS") if env("SETTINGS") else 'production'

env_file = f".envs/.{environment}/.django"
dotenv.read_dotenv(str(ROOT_DIR.path(env_file)))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'help_gamblers.settings.{environment}')

application = get_wsgi_application()
