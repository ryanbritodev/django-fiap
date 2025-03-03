from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Livro

# Create your views here.

# Resposta do servidor quando for chamado
def index(request):
    dados = {
        'livros': Livro.objects.all()
    }
    return render(request, 'index.html', dados)

def livro(request, livro_id):
    livro = {
        'livro': get_object_or_404(Livro, pk=livro_id)
    }
    return render(request, 'livro.html', livro)

def emprestimo(request):
    if not request.user.is_authenticated:
        return redirect('index')

    dados = {
        'livros': Livro.objects.filter(emprestado=False)
    }
    print(dados)
    return render(request, 'index.html', dados)

def busca(request):
    livros = Livro.objects.order_by('titulo').all() # Recuperação de todos os livros, ordenando pelo título

    # Se dentro da requisição que eu tiver feito, for um GET (feito pelo navegador de forma simples)...
    if 'titulo' in request.GET:
        # Vou pegar o título passado como parâmetro, em formato de dicionário
        titulo = request.GET['titulo']
        if titulo: # Se esse título for digitado
            livros = livros.filter(titulo__icontains=titulo) # Filtro que compara se aquele texto existe naquele título

    dados = {
        'livros': livros
    }
    return render(request, 'index.html', dados)