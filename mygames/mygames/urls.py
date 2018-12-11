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
    path('carrinho/add<int:jogo_id>', views.add_carrinho, name = 'add_carrinho'),
    path('carrinho/',views.carrinho,name='carrinho'),
    path('remover_jogo/<int:jogo_id>', views.remover_jogo, name='remover_jogo')
]
