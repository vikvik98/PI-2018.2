from django.shortcuts import render, redirect

from games.models import Jogo
from mygames.forms import DesenvolvedoraForm, PublicadoraForm, JogoForm


def home(request):
    jogos = Jogo.objects.all()
    return render(request,'home.html',{'jogos': jogos})


def add_jogo(request):
    if request.method =='POST':
        desenvolvedoraform = DesenvolvedoraForm(request.POST)
        publicadoraform = PublicadoraForm(request.POST)
        jogoform = JogoForm(request.POST)

        if desenvolvedoraform.is_valid() and publicadoraform.is_valid() and jogoform.is_valid():
            jogo_instance = jogoform.save()
            desenvolvedora_instance = desenvolvedoraform.save(commit=False)
            publicadora_instance = publicadoraform.save(commit=False)

            desenvolvedora_instance.jogo = jogo_instance
            desenvolvedora_instance.save()
            publicadora_instance.jogo = jogo_instance
            publicadora_instance.save()

            return redirect('home')

        else:
            desenvolvedoraform = DesenvolvedoraForm()
            publicadoraform = PublicadoraForm()
            jogoform = JogoForm()

            return render(request,'add_jogo.html',{'desenvolvedoraform':desenvolvedoraform,
                                                   'publicadoraform':publicadoraform,
                                                   'jogoform':jogoform})
    else:
        desenvolvedoraform = DesenvolvedoraForm()
        publicadoraform = PublicadoraForm()
        jogoform = JogoForm()

        return render(request, 'add_jogo.html', {'desenvolvedoraform': desenvolvedoraform,
                                                 'publicadoraform': publicadoraform,
                                                 'jogoform': jogoform})



def jogo(request, jogo_id):
    jogo = Jogo.objects.get(id = jogo_id)
    desenvolvedora = jogo.desenvolvedoras.all()
    publicadora = jogo.publicadoras.all()[0]
    return render(request,'jogo.html',{'jogo':jogo, 'desenvolvedora':desenvolvedora, 'publicadora':publicadora})


def carrinho(request):
    pass