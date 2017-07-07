from datetime import datetime

class Contato(object):
    def __init__(self, cId, cNome, cTelefone, cEndereco):
        self.id = cId
        self.nome = cNome
        self.telefone = cTelefone
        self.endereco = cEndereco


    def __repr__(self):
        return '{0},{1},{2},{3}'.format(self.id, self.nome, self.telefone, self.endereco)
