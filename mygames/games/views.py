from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect

from games.models import Jogo, Carrinho
from mygames import forms
from mygames.forms import DesenvolvedoraForm, PublicadoraForm, JogoForm



def verificar_carrinho():
    try :
        Carrinho.objects.get(finalizado = False)
    except Carrinho.DoesNotExist:
        carrinho = Carrinho()
        carrinho.save()

def home(request):
    jogos = Jogo.objects.all()
    return render(request, 'home.html', {'jogos': jogos})


def add_jogo(request):
    verificar_carrinho()
    if request.method == 'POST':
        desenvolvedoraform = DesenvolvedoraForm(request.POST)
        publicadoraform = PublicadoraForm(request.POST)
        jogoform = JogoForm(request.POST)

        if desenvolvedoraform.is_valid() and publicadoraform.is_valid() and jogoform.is_valid():
            jogo_instance = jogoform.save(commit=False)
            if jogo_instance.preco < 0:
                raise ValidationError(
                    "Não pode preço negativo"
                )

            if jogo_instance.quant_estoque < 0:
                raise ValidationError(
                    "Não pode estoque negativo"
                )
            if Jogo.objects.filter(nome = jogo_instance.nome):
                raise ValidationError(
                    "Não pode o nome do jogo repitido"
                )
            desenvolvedora_instance = desenvolvedoraform.save()
            publicadora_instance = publicadoraform.save()
            jogo_instance.desenvolvedora = desenvolvedora_instance
            jogo_instance.publicadora = publicadora_instance
            jogo_instance.save()

            return redirect('home')

        else:
            desenvolvedoraform = DesenvolvedoraForm()
            publicadoraform = PublicadoraForm()
            jogoform = JogoForm()

            return render(request, 'add_jogo.html', {'desenvolvedoraform': desenvolvedoraform,
                                                     'publicadoraform': publicadoraform,
                                                     'jogoform': jogoform})
    else:
        desenvolvedoraform = DesenvolvedoraForm()
        publicadoraform = PublicadoraForm()
        jogoform = JogoForm()

        return render(request, 'add_jogo.html', {'desenvolvedoraform': desenvolvedoraform,
                                                 'publicadoraform': publicadoraform,
                                                 'jogoform': jogoform})


def jogo(request, jogo_id):
    carrinho = Carrinho.objects.all()[0]
    jogo = Jogo.objects.get(id=jogo_id)
    desenvolvedora = jogo.desenvolvedora
    publicadora = jogo.publicadora
    return render(request, 'jogo.html', {'jogo': jogo, 'desenvolvedora': desenvolvedora, 'publicadora': publicadora,'carrinho': carrinho})


def add_carrinho(request, jogo_id):
    verificar_carrinho()
    carrinho = Carrinho.objects.get(finalizado = False)
    jogo = Jogo.objects.get(id = jogo_id)
    if jogo.quant_estoque > 0:
        jogo.quant_estoque = (jogo.quant_estoque - 1)
        jogo.save()
        carrinho.jogos_carrinho.add(jogo)
        jogos_carrinho = carrinho.jogos_carrinho.all()
        return render(request, 'carrinho.html', {'jogos_carrinho': jogos_carrinho})
    else:
        raise ValidationError(
                    "Não tem mais estoque deste jogo!"
                )


def carrinho(request):
    verificar_carrinho()
    carrinho = Carrinho.objects.get(finalizado=False)
    jogos_carrinho = carrinho.jogos_carrinho.all()
    return render(request, 'carrinho.html', {'jogos_carrinho': jogos_carrinho})

def remover_jogo(request, jogo_id):
    Jogo.objects.filter(id=jogo_id).delete()
    return redirect('home')



def remover_jogo_carrinho(request, jogo_id):
    verificar_carrinho()
    carrinho = Carrinho.objects.get(finalizado=False)
    jogo = Jogo.objects.get(id=jogo_id)
    carrinho.jogos_carrinho.remove(jogo)
    return redirect('carrinho')

def finalizar_compra(request):
    verificar_carrinho()
    carrinho = Carrinho.objects.get(finalizado=False)
    carrinho.finalizado = True
    carrinho.save()
    return redirect('meus_jogos')

def meus_jogos(request):
    jogos = []
    carrinhos_finalizados = Carrinho.objects.filter(finalizado = True)
    for carrinho_finalizado in carrinhos_finalizados:
        for jogo in carrinho_finalizado.jogos_carrinho.all():
            jogos.append(jogo)
    return render(request,'meus_jogos.html', {'jogos':jogos})

def editar_jogo(request, jogo_id):
    jogo = Jogo.objects.get(id=jogo_id)

    if request.method == 'POST':
        desenvolvedoraform = DesenvolvedoraForm(request.POST, instance=jogo.desenvolvedora)
        publicadoraform = PublicadoraForm(request.POST, instance=jogo.publicadora)
        jogoform = JogoForm(request.POST, instance=jogo)

        if desenvolvedoraform.is_valid() and publicadoraform.is_valid() and jogoform.is_valid():
            jogo_instance = jogoform.save(commit=False)
            if jogo_instance.preco < 0:
                raise ValidationError(
                    "Não pode preço negativo"
                )

            if jogo_instance.quant_estoque < 0:
                raise ValidationError(
                    "Não pode estoque negativo"
                )
            desenvolvedora_instance = desenvolvedoraform.save()
            publicadora_instance = publicadoraform.save()
            jogo_instance.desenvolvedora = desenvolvedora_instance
            jogo_instance.publicadora = publicadora_instance
            jogo_instance.save()

            return redirect('home')

        else:
            desenvolvedoraform = DesenvolvedoraForm(instance=jogo.desenvolvedora)
            publicadoraform = PublicadoraForm(instance=jogo.publicadora)
            jogoform = JogoForm(instance=jogo)

            return render(request, 'add_jogo.html', {'desenvolvedoraform': desenvolvedoraform,
                                                     'publicadoraform': publicadoraform,
                                                     'jogoform': jogoform})
    else:
        desenvolvedoraform = DesenvolvedoraForm(instance=jogo.desenvolvedora)
        publicadoraform = PublicadoraForm(instance=jogo.publicadora)
        jogoform = JogoForm(instance=jogo)

        return render(request, 'add_jogo.html', {'desenvolvedoraform': desenvolvedoraform,
                                                 'publicadoraform': publicadoraform,
                                                 'jogoform': jogoform})


def filtro_mais_caro(request):
    jogos = Jogo.objects.order_by('-preco')
    return render(request, 'home.html', {'jogos': jogos})

def filtro_mais_barato(request):
    jogos = Jogo.objects.order_by('preco')
    return render(request, 'home.html', {'jogos': jogos})

def filtro_alfabetico(request):
    jogos = Jogo.objects.order_by('nome')
    return render(request, 'home.html', {'jogos': jogos})

