"""mygames URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from games import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('add_jogo/', views.add_jogo, name='add_jogo'),
    path('jogo/<int:jogo_id>', views.jogo, name='jogo'),
    path('jogo/<int:jogo_id>/editar/', views.editar_jogo, name='editar_jogo'),
    path('carrinho/add<int:jogo_id>', views.add_carrinho, name = 'add_carrinho'),

    path('carrinho/',views.carrinho,name='carrinho'),
    path('remover_jogo/<int:jogo_id>', views.remover_jogo, name='remover_jogo'),
    path('remover_jogo_carrinho/<int:jogo_id>', views.remover_jogo_carrinho, name='remover_jogo_carrinho'),
    path('finalizar_compra', views.finalizar_compra, name = 'finalizar_compra'),
    path('meus_jogos', views.meus_jogos, name='meus_jogos'),

    path('remover_jogo/<int:jogo_id>', views.remover_jogo, name='remover_jogo'),
    path('filtro/mais_caro', views.filtro_mais_caro, name='filtro_mais_caro'),
    path('filtro/mais_barato', views.filtro_mais_barato, name='filtro_mais_barato'),
    path('filtro/alfabetico', views.filtro_alfabetico, name='filtro_alfabetico')

]
