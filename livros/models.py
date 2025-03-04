from django.db import models
from autores.models import Autor

# Criando nosso modelo com uma classe
# Precisamos importar o módulo "models"


class Livro(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE) # Chave estrangeira, ao deletar na minha tabela principal, também é deletado na tabela autor (efeito cascata)
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    paginas = models.IntegerField()
    editora = models.CharField(max_length=50)
    edicao = models.IntegerField()
    ano_publicacao = models.IntegerField()
    emprestado = models.BooleanField(default=False)
    capa = models.ImageField(upload_to='capas/%Y/%m/%d', blank=True) # Vai nos trazer dia/mês/ano da capa e caso não tiver capa, vai aparecer nula
    idioma = models.CharField(max_length=20)
    isbn = models.CharField(max_length=20)

    def __str__(self):
        return self.titulo  # Forma que ele aparecerá no console de admin (seu nome, e não a instância da classe)
