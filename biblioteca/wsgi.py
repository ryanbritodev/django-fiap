"""
WSGI config for biblioteca project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'biblioteca.settings')
django.setup()

from django.core.management import call_command

# Criar/migrar banco de dados ao iniciar a aplicação
if not os.path.exists('/tmp/db.sqlite3'):
    call_command('migrate')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
app = application

