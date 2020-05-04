from application.model.entity.usuario import Usuario

class Autor(Usuario):
    def __init__(self, publicacao = []):
        self._publicacao = publicacao

    def get_publicacao(self):
        return self._publicacao

    def set_publicacao(self,nova_publicacao):
        self._publicacao.append(nova_publicacao)