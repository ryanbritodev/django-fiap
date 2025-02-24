from django.contrib import admin
from .models import Autor


# Criando nossa classe para exibição dos autores
class ExibeAutor(admin.ModelAdmin): # Recebe como parâmetro o ModelAdmin, responsável por mostrar as informações dos dados na nossa parte administrativa
    list_display = ('id', 'nome', 'nacionalidade') # O que eu quero mostrar
    list_display_links = ('id', 'nome') # Quais atributos vou poder clicar pra acessar os detalhes
    search_fields = ('nome',) # Pelo o que buscar na base de dados para mostrar (colocar vírgula por ser uma tupla com um item)
    list_filter = ('nacionalidade',) # Filtro pelo ano de publicação
    list_per_page = 2 # 2 livros por página


# Registrando o nosso modelo
# Vai se tornar visível dentro do nosso app de administração

admin.site.register(Autor, ExibeAutor) # Realizar o registro
