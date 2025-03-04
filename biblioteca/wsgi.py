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
from django.contrib.auth import get_user_model

# Criar/migrar banco de dados automaticamente
if not os.path.exists('/tmp/db.sqlite3'):
    call_command('migrate')  # Aplica as migrações

# Criar superusuário automaticamente se ele não existir
User = get_user_model()

try:
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='admin',
            email='admin@admin.com',
            password='admin'
        )
        print("Superusuário criado com sucesso!")
except Exception as e:
    print(f"Erro ao criar superusuário: {e}")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
app = application
