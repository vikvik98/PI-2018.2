# Generated by Django 2.1.4 on 2018-12-11 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_auto_20181210_2204'),
    ]

    operations = [
        migrations.AddField(
            model_name='jogo',
            name='preco',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='jogo',
            name='quant_estoque',
            field=models.IntegerField(default=0),
        ),
    ]
