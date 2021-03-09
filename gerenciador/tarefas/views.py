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


def usuario(request, usuario_id):
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


def atualizarUsuario(request, usuario_id):
    if request.method == 'POST':
        novo_nome = request.POST['novo_nome']
        if novo_nome.strip():
            usuarioDao.atualizarUsuario(Usuario(id=usuario_id, nome=novo_nome))
            return redirect('listaUsuarios')
        else:
            return redirect('paginaErro', "nome em branco")
    else:
        usuario = usuarioDao.getUsuario(int(usuario_id))
        return render(request, 'AtualizarUsuario.html', {'usuario': usuario})


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
            descricao = request.POST['descricao']
            if descricao.strip():
                tarefa = Tarefa(descricao=descricao, concluido=bool(request.POST['estado_tarefa']),
                                usuario=Usuario.objects.get(pk=int(request.POST['id_usuario'])))
                tarefasDao.criarTarefa(tarefa)
                return redirect('listaTarefas')
            else:
                return redirect('criarTarefa')
        except:
            return redirect('paginaErro')
    else:
        usuarios = usuarioDao.getTodosUsuarios()
        return render(request, 'CriarTarefa.html', {'lista': usuarios})


def atualizarTarefa(request, id_tarefa):
    if request.method == 'POST':
        if 'atualizar_estado' in request.POST['acao']:
            if 'Feito' in request.POST['novo_estado']:
                novo_estado = True
            else:
                novo_estado = False
            tarefasDao.atualizarEstadoTarefa(id_tarefa, novo_estado)
            return redirect('listaTarefas')
        else:
            descricao = request.POST['descricao']
            if descricao.strip():
                tarefa = Tarefa(id=id_tarefa, descricao=descricao, concluido=bool(request.POST['estado_tarefa']),
                                usuario=Usuario.objects.get(pk=int(request.POST['id_usuario'])))
                tarefasDao.atualizarTarefa(tarefa)
                return redirect('listaTarefas')
            else:
                return redirect('criarTarefa')
    else:
        tarefa = tarefasDao.getTarefa(id_tarefa)
        usuarios = usuarioDao.getTodosUsuarios()
        return render(request, 'AtualizarTarefa.html', {'tarefa': tarefa, 'usuarios': usuarios})


def paginaErro(request, message):
    return render(request, 'PaginaErro.html', {'message': message})
