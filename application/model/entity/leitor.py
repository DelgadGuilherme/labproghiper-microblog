from application.model.entity.usuario import Usuario

class Leitor(Usuario):
    def __init__(self, autor_seguido = [], publicacao_curtida = []):
        self._autor_seguido = autor_seguido
        self._publicacao_curtida = publicacao_curtida

    def get_autor_seguido(self):
        return self._autor_seguido

    def get_publicacao_curtida(self):
        return self._publicacao_curtida

    def set_autor_curtido(self, novo_autor):
        self._autor_seguido.append(novo_autor)

    def set_publicacao_curtida(self, nova_curtida):
        self._publicacao_curtida.append(nova_curtida)