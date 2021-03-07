from django.urls import path

from . import views

urlpatterns = [
    path('', views.listaUsuarios, name='listaUsuarios'),
    path('Usuario', views.usuario, name='usuario'),
    path('CriarUsuario', views.criarUsuario, name='criarUsuario'),
    path('ListaAtividades', views.listaAtividades, name='listaAtividades'),
    path('CriarAtividade', views.criarAtividade, name='criarAtividade')
]
