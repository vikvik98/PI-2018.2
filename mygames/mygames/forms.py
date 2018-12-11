from django.forms import ModelForm

from games.models import Desenvolvedora, Publicadora, Jogo


class DesenvolvedoraForm(ModelForm):
    class Meta:
        model = Desenvolvedora
        fields = ['nome_desenvolvedora']



class PublicadoraForm(ModelForm):
    class Meta:
        model = Publicadora
        fields = ['nome_publicadora']


class JogoForm(ModelForm):
    class Meta:
        model = Jogo
        fields = ['nome','preco','quant_estoque','descricao']


