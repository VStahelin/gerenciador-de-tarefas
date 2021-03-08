from django.shortcuts import render, redirect

from .dao import usuarioDao, tarefasDao
from .models import Usuario, Tarefa


def dashboard(request):
    dict = {
        'tota_usuarios': usuarioDao.getTotalUsuarios(),
        'total_tarefas': tarefasDao.getTotalTarefas(),
        'total_tarefas_pendentes': tarefasDao.getTotalTarefasPendentes(),
        'total_tarefas_feitas': tarefasDao.getTotalTarefasPendentes()
    }
    return render(request, 'Dashboard.html', dict)


def listaUsuarios(request):
    usuarios = usuarioDao.getTodosUsuarios()
    return render(request, 'ListaUsuarios.html', {'lista': usuarios})


def usuario(request):
    usuario_id = int(request.POST['usuario_id'])
    dados = {'usuario': usuarioDao.getUsuario(usuario_id),
             'tarefas': tarefasDao.getTarefasPorUsuario(usuario_id),
             'total_tarefas': tarefasDao.getTotalTarefasPorUsuario(usuario_id),
             'total_tarefas_feitas': tarefasDao.getTotalTarefasPorUsuarioFeitas(usuario_id),
             'total_tarefas_pendentes': tarefasDao.getTotalTarefasPorUsuarioPendentes(usuario_id)
             }
    return render(request, 'Usuario.html', dados)


def criarUsuario(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        if nome.strip():
            usuarioDao.createUsuario(nome)
            return redirect('listaUsuarios')
        else:
            return redirect('criarUsuario')
    else:
        return render(request, 'CriarUsuario.html')


def deletarUsuario(request):
    if request.method == 'POST':
        try:
            usuarioDao.deleteUsuario(request.POST['id_usuario'])
            return redirect('listaUsuarios')
        except:
            return redirect('paginaErro')


def deletarTarefa(request):
    if request.method == 'POST':
        try:
            tarefasDao.deleteTarefa(request.POST['id_tarefa'])
            return redirect('listaTarefas')
        except:
            return redirect('paginaErro')

    else:
        redirect('listaUsuarios')


def listaTarefas(request):
    tarefas = tarefasDao.getTarefas()
    return render(request, 'ListaTarefa.html', {'lista': tarefas})


def criarTarefa(request):
    if request.method == 'POST':
        try:
            tarefa = Tarefa(descricao=request.POST['descricao'], concluido=bool(request.POST['estado_tarefa']),
                            user=Usuario.objects.get(pk=int(request.POST['id_usuario'])))
            tarefasDao.criarTarefa(tarefa)
            return redirect('listaTarefas')
        except:
            return redirect('paginaErro')
    else:
        usuarios = usuarioDao.getTodosUsuarios()
        return render(request, 'CriarTarefa.html', {'lista': usuarios})


def atualizarTarefa(request):
    if request.method == 'POST':
        # try:
            id_tarefa = int(request.POST['id_tarefa'])
            if 'Feito' in request.POST['novo_estado']:
                novo_estado = True
            else:
                novo_estado = False
            tarefasDao.atualizarTarefa(id_tarefa, novo_estado)
            return redirect('listaTarefas')
        # except:
        #     return redirect('paginaErro')


def paginaErro(request):
    return render(request, 'PaginaErro.html')
