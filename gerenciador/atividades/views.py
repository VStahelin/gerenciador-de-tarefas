from django.shortcuts import render

from django.http import HttpResponse


def listaUsuarios(request):
    return render(request, 'ListaUsuarios.html')


def usuario(request):
    return render(request, 'Usuario.html')

def criarUsuario(request):
    return render(request, 'CriarUsuario.html')

def listaAtividades(request):
    return render(request, 'ListaAtividades.html')

def criarAtividade(request):
    return render(request, 'CriarAtividade.html')