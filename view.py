from tkinter import *

class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.quintoContainer = Frame(master)
        self.quintoContainer["padx"] = 20
        self.quintoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Agenda de Contatos")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.nomeLabel = Label(self.segundoContainer,text="Nome", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)

        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)

        self.senhaLabel = Label(self.terceiroContainer, text="Telefone", font=self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)

        self.senha = Entry(self.terceiroContainer)
        self.senha["width"] = 30
        self.senha["font"] = self.fontePadrao
        self.senha["show"] = "*"
        self.senha.pack(side=LEFT)


        self.enderecoLabel = Label(self.quartoContainer, text="Endereço", font=self.fontePadrao)
        self.enderecoLabel.pack(side=LEFT)

        self.endereco = Entry(self.quartoContainer)
        self.endereco["width"] = 30
        self.endereco["font"] = self.fontePadrao
        self.endereco["show"] = "*"
        self.endereco.pack(side=LEFT)

        self.cadastrar = Button(self.quintoContainer)
        self.cadastrar["text"] = "Autenticar"
        self.cadastrar["font"] = ("Calibri", "8")
        self.cadastrar["width"] = 12
    #    self.cadastrar["command"] = self.verificaSenha
    #    self.cadastrar.pack()

        self.mensagem = Label(self.quintoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

    '''#Método verificar senha
    def verificaSenha(self):
        usuario = self.nome.get()
        senha = self.senha.get()
        if usuario == "usuariodevmedia" and senha == "dev":
            self.mensagem["text"] = "Autenticado"
        else:
            self.mensagem["text"] = "Erro na autenticação"'''

root = Tk()
Application(root)
root.mainloop()
