from django.db import models


class Desenvolvedora(models.Model):
    nome_desenvolvedora = models.CharField(max_length=100)




class Publicadora(models.Model):
    nome_publicadora = models.CharField(max_length=100)



class Jogo(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.FloatField(default=0)
    descricao = models.TextField(default="Miau")
    quant_estoque = models.IntegerField(default=0)
    desenvolvedora = models.ForeignKey(Desenvolvedora, on_delete=models.CASCADE, related_name='jogos')
    publicadora = models.ForeignKey(Publicadora, on_delete=models.CASCADE, related_name='jogos')


class Carrinho(models.Model):
    finalizado = models.BooleanField(default=False)
    jogos_carrinho = models.ManyToManyField(Jogo)