from model import Contato
from datetime import datetime

class CtrlContato(object):
    def __init__(self):
        self.__contatos = {}
        self.__ultIdContato = 0

    def __getIdNovoContato(self):
        self.__ultIdContato +=1
        return self.__ultIdContato

    def __getContato(self, cId):
        if not (cId in self.__contatos):
            raise Exception('Contato com o identificador não encontrado.')

        return self.__contatos[cId]

    def listaContatos(self):
        return (self.__contatos)

#operações na Agenda

    def addContato(self, cNome, cTelefone, cEndereco):
        c = Contato(self.__getIdNovoContato(),cNome, cTelefone, cEndereco)

        self.__contatos[c.id] = c

#*************** Código de Teste ****************#

if __name__ == "__main__":
    c = CtrlContato()
    c.addContato('Victor','999999999','Rua 10 - Jussara')
    c.addContato('Jefferson','111111111','Rua 11 - Tamboraí')

    listC = c.listaContatos()
    for c in listC:
        print(listC[c])
