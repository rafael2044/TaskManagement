import customtkinter as ctk
from classes.Tarefa import Tarefa
from widgets.WidgetTarefa import WidgetTarefa
from telas.TelaNovaTarefa import TelaNovaTarefa
from models.TarefaModel import TarefaModel
class TelaPrincipal(ctk.CTk):
    def __init__(self):
        super(TelaPrincipal, self).__init__()
        self.emExibicao = True
        self.telaNovaTarefa = None
        self.tarefas = None
        self.widgetsTarefa = None
        self.configurarTela()
        self.carregarWidgets()
        self.exibirWidgets()
        self.carregarTarefas()
        self.carregarTarefas()
        self.exibirAllTarefas()

        self.mainloop()

    def configurarTela(self):
        ctk.set_appearance_mode("dark")
        WIDTH = 800
        HEIGHT = 600
        POS_X = (self.winfo_screenwidth() - WIDTH) // 2
        POS_Y = (self.winfo_screenheight() - HEIGHT) // 2

        self.geometry(f"{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}")
        self.title("Task Management")
    def carregarWidgets(self):
        self.fontLabel = ctk.CTkFont(family='dubai medium', size=20, weight='bold')
        self.fontButton = ctk.CTkFont(family='dubai medium', size=16, weight='bold')
        self.frMain = ctk.CTkFrame(self)
        self.frHeader = ctk.CTkFrame(self.frMain, height=50)
        self.frFilter = ctk.CTkFrame(self.frMain, height=50)
        self.frContent = ctk.CTkScrollableFrame(self.frMain)


        self.lbTitulo = ctk.CTkLabel(self.frHeader, text='Tarefas que você precisa fazer',
                                     font=self.fontLabel)
        self.btNovaTarefa = ctk.CTkButton(self.frHeader, text='Nova Tarefa',
                                          font=self.fontButton, command=self.exibirTelaNovaTarefa)



    def exibirWidgets(self):
        self.frMain.pack(expand=True, fill=ctk.BOTH)
        self.frHeader.pack(fill=ctk.X, side=ctk.TOP)
        self.frFilter.pack(fill=ctk.X, side=ctk.TOP)
        self.frContent.pack(expand=True, fill=ctk.BOTH)

        self.lbTitulo.pack(side=ctk.LEFT, anchor=ctk.W, padx=5, pady=10)
        self.btNovaTarefa.pack(anchor=ctk.E, padx=5, pady=10)

    def carregarTarefas(self):
        self.tarefas = [Tarefa(x.id,x.nomeTarefa,x.prioridadeTarefa.nomePrioridade, x.dataHoraTarefa,
                               x.statusTarefa.nomeStatus) for x in TarefaModel.select().execute()]
        self.widgetsTarefa = []
        if len(self.tarefas) != 0:
            for t in self.tarefas:
                self.widgetsTarefa.append(WidgetTarefa(self.frContent,self, t))

    def exibirAllTarefas(self):
        if len(self.widgetsTarefa) != 0:
            for wt in self.widgetsTarefa:
                wt.pack(fill=ctk.X, side=ctk.TOP, padx=10, pady=5)

    def adicionarNovaTarefa(self):
        if len(self.tarefas) > 0:
            ultimaTarefaAtual = self.tarefas[-1]
            novaTarefa = [Tarefa(x.id,x.nomeTarefa,x.prioridadeTarefa.nomePrioridade, x.dataHoraTarefa,
                                   x.statusTarefa.nomeStatus) for x in TarefaModel.select().where(TarefaModel.id == ultimaTarefaAtual.getId()+1)][0]
            self.tarefas.append(novaTarefa)
            widgetNovaTarefa = WidgetTarefa(self.frContent,self, novaTarefa)
            self.widgetsTarefa.append(widgetNovaTarefa)
            widgetNovaTarefa.pack(fill=ctk.X, side=ctk.TOP, padx=10, pady=5)
        else:
            novaTarefa = [Tarefa(x.id,x.nomeTarefa,x.prioridadeTarefa.nomePrioridade, x.dataHoraTarefa,
                                   x.statusTarefa.nomeStatus) for x in TarefaModel.select().where(TarefaModel.id == 1)][0]
            self.tarefas.append(novaTarefa)
            widgetNovaTarefa = WidgetTarefa(self.frContent,self, novaTarefa)
            self.widgetsTarefa.append(widgetNovaTarefa)
            widgetNovaTarefa.pack(fill=ctk.X, side=ctk.TOP, padx=10, pady=5)
    def exibirTelaNovaTarefa(self):
        self.ocultarTela()

        if self.telaNovaTarefa == None or not self.telaNovaTarefa.emExibicao:
            tela = TelaNovaTarefa(self)
            tela.pack(fill=ctk.BOTH, expand=True)
        else:
            self.telaNovaTarefa.reexibirTela()

    def ocultarTela(self):
        if self.emExibicao:
            self.frMain.forget()
            self.emExibicao = False

    def reexibirTela(self):
        if not self.emExibicao:
            self.frMain.pack(fill=ctk.BOTH, expand=True)
            self.emExibicao = True

    def excluirTarefaEWidget(self, wtarefa):
        self.tarefas.remove(wtarefa.tarefa)
        self.widgetsTarefa.remove(wtarefa)
        wtarefa.destroy()

