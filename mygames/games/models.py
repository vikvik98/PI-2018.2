from django.db import models

class Desenvolvedora(models.Model):
    nome = models.CharField(max_length=100)
    fundacao = models.DateField()



class Publicadora(models.Model):
    nome = models.CharField(max_length=100)



class Jogo(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.FloatField(default=0)
    quant_estoque = models.IntegerField(default=0)
    desenvolvedoras = models.ManyToManyField(Desenvolvedora, through='Desenvolvimento_jogo')
    publicadoras = models.ManyToManyField(Publicadora, through='Publicacao_jogo')


class Desenvolvimento_jogo(models.Model):
    desenvolvedora = models.ForeignKey(Desenvolvedora, on_delete=models.CASCADE)
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)
    inicio_desenvolvimento = models.DateField()
    termino_desenvolvimento = models.DateField()



class Publicacao_jogo(models.Model):
    publicadora = models.ForeignKey(Publicadora, on_delete=models.CASCADE)
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)
    data_publicacao = models.DateField()


class Carrinho:
    pass
