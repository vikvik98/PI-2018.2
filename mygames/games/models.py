from django.db import models

class Desenvolvedora(models.Model):
    nome = models.CharField(max_length=100)
    fundacao = models.DateField()



class Publicadora(models.Model):
    nome = models.CharField(max_length=100)



class Avaliadora(models.Model):
    nome = models.CharField(max_length=100)




class Jogo(models.Model):
    nome = models.CharField(max_length=100)
    desenvolvedoras = models.ManyToManyField(Desenvolvedora, through='Desenvolvimento_jogo')
    publicadoras = models.ManyToManyField(Publicadora, through='Publicacao_jogo')
    avaliacao = models.ManyToManyField(Avaliadora, through='Avaliacao_jogo')



class Desenvolvimento_jogo(models.Model):
    desenvolvedora = models.ForeignKey(Desenvolvedora, on_delete=models.CASCADE)
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)
    inicio_desenvolvimento = models.DateField()
    termino_desenvolvimento = models.DateField()



class Publicacao_jogo(models.Model):
    publicadora = models.ForeignKey(Publicadora, on_delete=models.CASCADE)
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)
    data_publicacao = models.DateField()


class Avaliacao_jogo(models.Model):
    avaliadora = models.ForeignKey(Avaliadora, on_delete=models.CASCADE)
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)
    nota = models.FloatField()