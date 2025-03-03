from django.contrib import admin
from .models import Livro


# Criando nossa classe para exibição dos livros na tela de administrador
class ExibeLivro(admin.ModelAdmin): # Recebe como parâmetro o ModelAdmin, responsável por mostrar as informações dos dados na nossa parte administrativa
    list_display = ('id', 'titulo', 'ano_publicacao', 'autor', 'emprestado') # O que eu quero mostrar
    list_display_links = ('id', 'titulo') # Quais atributos vou poder clicar pra acessar os detalhes
    search_fields = ('titulo',) # Pelo o que buscar na base de dados para mostrar (colocar vírgula por ser uma tupla com um item)
    list_filter = ('ano_publicacao',) # Filtro pelo ano de publicação
    list_editable = ('emprestado',) # Definindo o valor editável (booleano) emprestado
    list_per_page = 2 # 2 livros por página


# Registrando o nosso modelo
# Vai se tornar visível dentro do nosso app de administração

admin.site.register(Livro, ExibeLivro) # Realizar o registro
