from django.forms import ModelForm

from games.models import Desenvolvedora, Publicadora, Jogo, Desenvolvimento_jogo, Publicacao_jogo


class DesenvolvedoraForm(ModelForm):
    class Meta:
        model = Desenvolvedora
        fields = ['nome','fundacao']



class PublicadoraForm(ModelForm):
    class Meta:
        model = Publicadora
        fields = ['nome']


class JogoForm(ModelForm):
    class Meta:
        model = Jogo
        fields = ['nome','preco','quant_estoque']


class DesenvolvimentoForm(ModelForm):
    class Meta:
        model = Desenvolvimento_jogo
        fields = ['inicio_desenvolvimento', 'termino_desenvolvimento']


class PublicacaoForm(ModelForm):
    class Meta:
        model = Publicacao_jogo
        fields = ['data_publicacao']