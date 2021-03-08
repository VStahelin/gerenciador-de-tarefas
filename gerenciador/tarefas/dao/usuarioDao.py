from ..models import Usuario


def getTodosUsuarios():
    return Usuario.objects.all()

def getTotalUsuarios():
    return Usuario.objects.all().count()


def getUsuario(id):
    return Usuario.objects.get(id=id)


def createUsuario(nome):
    Usuario.objects.create(nome=nome)


def deleteUsuario(id):
    Usuario.objects.filter(id=id).delete()
