from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('Dashboard', views.dashboard, name='dashboard'),
    path('ListaUsuarios', views.listaUsuarios, name='listaUsuarios'),
    path('Usuario', views.usuario, name='usuario'),
    path('CriarUsuario', views.criarUsuario, name='criarUsuario'),
    path('ListaTarefas', views.listaTarefas, name='listaTarefas'),
    path('CriarTarefa', views.criarTarefa, name='criarTarefa'),
    path('DeletarTarefa', views.deletarTarefa, name='deletarTarefa'),
    path('DeletarUsuario', views.deletarUsuario, name='deletarUsuario'),
    path('PaginaErro', views.paginaErro, name='paginaErro'),
    path('AtualizarTarefa', views.atualizarTarefa, name='atualizarTarefa')
]
