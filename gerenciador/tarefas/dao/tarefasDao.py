from ..models import Tarefa


def getTarefa(id):
    return Tarefa.objects.get(id=id)


def getTotalTarefasPorUsuario(usuario_id):
    return Tarefa.objects.filter(usuario=usuario_id).count()


def getTotalTarefasPorUsuarioFeitas(usuario_id):
    return Tarefa.objects.filter(usuario=usuario_id, concluido=True).count()


def getTotalTarefasPorUsuarioPendentes(usuario_id):
    return Tarefa.objects.filter(usuario=usuario_id, concluido=False).count()


def getTotalTarefas():
    return Tarefa.objects.all().count()


def getTotalTarefasFeitas():
    return Tarefa.objects.filter(concluido=True).count()


def getTotalTarefasPendentes():
    return Tarefa.objects.filter(concluido=False).count()


def getTarefas():
    return Tarefa.objects.all()


def getTarefasPorUsuario(usuario_id):
    return Tarefa.objects.filter(usuario=usuario_id)


def deleteTarefa(id_tarefa):
    Tarefa.objects.filter(id=id_tarefa).delete()


def criarTarefa(tarefa):
    tarefa.save()


def atualizarEstadoTarefa(tarefa_id, novo_estado):
    Tarefa.objects.filter(id=tarefa_id).update(concluido=novo_estado)


def atualizarTarefa(tarefa):
    Tarefa.objects.filter(id=tarefa.id).update(descricao=tarefa.descricao, concluido=tarefa.concluido,
                                               usuario=tarefa.usuario)
