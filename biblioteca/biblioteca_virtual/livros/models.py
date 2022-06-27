from unittest.mock import DEFAULT
from django.db import models
from .views import cadastro
# Create your models here.
"""
class Cadastro_users(models.Model):
    GENDER = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro/Prefiro não informar'),
    )
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    email = models.EmailField()
    senha = models.CharField(max_length=16)
    nascimento = models.DateField()
    genero = models.CharField(max_length=9, choices=GENDER)

    def __str__(self):
        return self.nome
"""   

class Cadastro_livros(models.Model):
    IDIOMAS = (
        ('PT-BR', 'Português do Brasil'),
        ('PT-PT', 'Português de Portugal'),
        ('EN', 'Inglês'),
        ('ES', 'Espanhol'),
    )

    DISPONIVEL = (
        ('SIM', 'Sim'),
        ('NAO', 'Não'),
    )
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    sub_titulo = models.CharField(max_length=200)
    ISBN_10 = models.IntegerField()
    ISBN_13 = models.IntegerField()
    autor = models.CharField(max_length=200, unique=True, null=True)
    editora = models.CharField(max_length=200)
    ano = models.IntegerField()
    paginas = models.IntegerField()
    idioma = models.CharField(max_length=20, choices=IDIOMAS)
    sinopse = models.TextField()
    status = models.CharField(max_length=4, choices=DISPONIVEL)
    # generos =

    def __str__(self) -> str:
        return self.titulo

"""
#class Emprestimo(models.Model):
    id_emprestimo = models.AutoField(primary_key=True)
    id_livro = models.ForeignKey(Cadastro_livros, on_delete=models.CASCADE)
    id_user = models.ForeignKey(cadastro, on_delete=models.CASCADE)
    data_emprestimo = models.DateTimeField()
    data_retorno = models.DateTimeField()"""

# --------------------------------------------------------------------------------------------------
#  Emprestimo dando errado pq usuario deve ser um model, arranjar outra forma de cadastrar usuarios
# --------------------------------------------------------------------------------------------------