from django.db import models

class Jogo(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.FloatField(default=0)
    quant_estoque = models.IntegerField(default=0)

class Desenvolvedora(models.Model):
    nome = models.CharField(max_length=100)
    jogo = models.ForeignKey(Jogo,on_delete=models.CASCADE, related_name='desenvolvedoras')



class Publicadora(models.Model):
    nome = models.CharField(max_length=100)
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE, related_name='publicadoras')


class Carrinho(models.Model):
    finalizado = models.BooleanField(default=False)
    jogos_carrinho = models.ManyToManyField(Jogo)



