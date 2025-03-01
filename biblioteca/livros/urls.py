from django.urls import path
from . import views

# Views (arquivos responsáveis pelo comportamamento e processamento das rotas)
urlpatterns = [
    path('', views.index, name='index'),
    path('livro/<int:livro_id>/', views.livro, name='livro'),
]

# Espaço vazio seria do "path" algo como:
# http://localhost:8000/
# No caso, nossa raíz

# Depois passamos qual o método que ele vai processar

# name será o apelido do nosso arquivo