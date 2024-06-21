import customtkinter as ctk
from models.PrioridadeModel import PrioridadeModel
from models.TarefaModel import TarefaModel
from models.StatusModel import StatusModel
class TelaNovaTarefa(ctk.CTkFrame):
    def __init__(self, master):
        super(TelaNovaTarefa, self).__init__(master)
        self.emExibicao = True
        self.carregarWidgets()
        self.exibirWidgets()


    def carregarWidgets(self):
        self.fontText = ctk.CTkFont(family='dubai medium', size=20)
        self.fontButton = ctk.CTkFont(family='dubai medium', size=16, weight='bold')
        PRIORIDADES = [x.nomePrioridade for x in PrioridadeModel.select().execute()]
        self.btVoltar = ctk.CTkButton(self, text='Voltar', command=self.ocultarTela,
                                      font=self.fontButton)
        self.entryNovaTarefa = ctk.CTkEntry(self, placeholder_text='Digite sua nova tarefa...',
                                            font=self.fontText)
        self.cbPrioridade = ctk.CTkComboBox(self, values = PRIORIDADES)
        self.cbPrioridade.configure(state='readonly')

        self.btCriarNovaTarefa = ctk.CTkButton(self, font=self.fontButton, text='Criar Tarefa',
                                               command=self.adicionarNovaTarefa)
    def exibirWidgets(self):
        self.btVoltar.pack(anchor=ctk.W, side=ctk.TOP)
        self.entryNovaTarefa.pack(fill=ctk.X, padx=10, pady=(20,5))
        self.cbPrioridade.pack(padx=10, anchor=ctk.W)
        self.btCriarNovaTarefa.pack(pady=10)
    def adicionarNovaTarefa(self):
        if self.entryNovaTarefa.get():
            novaTarefa = {'nomeTarefa':self.entryNovaTarefa.get(),
                          'prioridadeTarefa':[x.id for x in PrioridadeModel.select(PrioridadeModel.id).where(PrioridadeModel.nomePrioridade == self.cbPrioridade.get())][0],
                          'statusTarefa' : [x.id for x in StatusModel.select(StatusModel.id).where(StatusModel.nomeStatus == 'Pendente')][0] }
            print(novaTarefa)
            TarefaModel.create(**novaTarefa)
            self.master.adicionarNovaTarefa()
    def ocultarTela(self):
        if self.emExibicao:
            self.forget()
            self.emExibicao = False
        self.master.reexibirTela()
    def reexibirTela(self):
        if not self.emExibicao:
            self.pack(fill=ctk.BOTH, expand=True)
            self.emExibicao=True