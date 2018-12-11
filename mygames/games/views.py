from django.shortcuts import render, redirect

from games.models import Jogo
from mygames.forms import DesenvolvedoraForm, PublicadoraForm, JogoForm, DesenvolvimentoForm, PublicacaoForm


def home(request):
    jogos = Jogo.objects.all()
    return render(request,'home.html',{'jogos': jogos})


def add_jogo(request):
    if request.method =='POST':
        desenvolvedoraform = DesenvolvedoraForm(request.POST)
        publicadoraform = PublicadoraForm(request.POST)
        jogoform = JogoForm(request.POST)
        desenvolvimentoform = DesenvolvimentoForm(request.POST)
        publicacaoform = PublicacaoForm(request.POST)

        if desenvolvedoraform.is_valid() and publicadoraform.is_valid() and jogoform.is_valid() and desenvolvimentoform.is_valid() and  publicacaoform.is_valid():
            desenvolvedora_instance = desenvolvedoraform.save()
            publicadora_instance = publicadoraform.save()
            jogo_instance = jogoform.save()
            desenvolvimento_instance = desenvolvimentoform.save(commit=False)
            publicacao_instance = publicadoraform.save(commit=False)

            desenvolvimento_instance.jogo = jogo_instance
            desenvolvimento_instance.desenvolvedora = desenvolvedora_instance
            desenvolvimento_instance.save()

            publicacao_instance.publicadora = publicadora_instance
            publicacao_instance.jogo = jogo_instance
            publicacao_instance.save()
            return redirect('home')

        else:
            desenvolvedoraform = DesenvolvedoraForm()
            publicadoraform = PublicadoraForm()
            jogoform = JogoForm()
            desenvolvimentoform = DesenvolvimentoForm()
            publicacaoform = PublicacaoForm()
            return render(request,'add_jogo.html',{'desenvolvedoraform':desenvolvedoraform,
                                                   'publicadoraform':publicadoraform,
                                                   'jogoform':jogoform,
                                                   'desenvolvimentoform':desenvolvimentoform,
                                                   'publicacaoform':publicacaoform})
    else:
        desenvolvedoraform = DesenvolvedoraForm()
        publicadoraform = PublicadoraForm()
        jogoform = JogoForm()
        desenvolvimentoform = DesenvolvimentoForm()
        publicacaoform = PublicacaoForm()
        return render(request, 'add_jogo.html', {'desenvolvedoraform': desenvolvedoraform,
                                                 'publicadoraform': publicadoraform,
                                                 'jogoform': jogoform,
                                                 'desenvolvimentoform': desenvolvimentoform,
                                                 'publicacaoform': publicacaoform})

