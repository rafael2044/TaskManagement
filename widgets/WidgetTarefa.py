import customtkinter as ctk
from classes.Tarefa import Tarefa
class WidgetTarefa(ctk.CTkFrame):
    def __init__(self, master, tarefa:Tarefa):
        super().__init__(master)
        self.PRIORIDADES = {'Alta': {'id': 3, 'color': 'red'},
                            'Media': {'id': 2, 'color': 'yellow'},
                            'Baixa': {'id': 1, 'color': 'green'}}
        self.tarefa = tarefa
        self.configurarFrame()
        self.carregarWidgets()
        self.exibirWidgets()
    def configurarFrame(self):
        self.configure(height=50)
        self.configure(corner_radius=30)

    def carregarWidgets(self):
        self.fontText = ctk.CTkFont(family='dubai medium', size=20, weight='bold')
        self.fontData = ctk.CTkFont(family='dubai medium', size=12, weight='bold')
        self.vStatus = ctk.StringVar()
        self.vStatus.set(self.tarefa.getStatus())

        self.frLeft = ctk.CTkFrame(self, bg_color='transparent', fg_color='transparent')
        self.frRight = ctk.CTkFrame(self, bg_color='transparent', fg_color='transparent')

        self.btPrioridade = ctk.CTkButton(self.frLeft, text='', corner_radius=150,
                                          width=30, height=30, command=self.alterarPrioridade)
        self.checarPrioridade()
        self.btExcluir = ctk.CTkButton(self.frLeft, text='X', width=30, height=30)
        self.cbStatus = ctk.CTkCheckBox(self.frLeft, text='', width=30, height=30,
                                        onvalue='Finalizada', offvalue='Pendente',
                                        variable=self.vStatus)
        self.lbNomeTarefa = ctk.CTkLabel(self.frRight, text=self.tarefa.getNome(), font=self.fontText)
        self.lbDataHora = ctk.CTkLabel(self.frRight, text=self.tarefa.getDataHora(),
                                       font=self.fontData)

    def exibirWidgets(self):
        self.frLeft.pack(side=ctk.LEFT, padx=(10,0), pady=5)
        self.frRight.pack(side=ctk.LEFT, fill=ctk.X, padx=(0,10), pady=5)

        self.btPrioridade.pack(side=ctk.LEFT, padx=5, pady=10)
        self.btExcluir.pack(side=ctk.LEFT, padx=(0,5), pady=10)
        self.cbStatus.pack(side=ctk.LEFT, padx=(0,5), pady=10)

        self.lbNomeTarefa.pack(anchor=ctk.W, padx=10, pady=(10,5))
        self.lbDataHora.pack(anchor=ctk.W, padx=10, pady=(5,10))

    def checarPrioridade(self):


        self.btPrioridade.configure(fg_color=self.PRIORIDADES[self.tarefa.getPrioridade()]['color'])
        self.btPrioridade.configure(hover_color=self.PRIORIDADES[self.tarefa.getPrioridade()]['color'])

    def alterarPrioridade(self):
        PRIORIDADES_ID = {1: 'Baixa', 2: 'Media', 3:'Alta'}
        idPrioridade = self.PRIORIDADES[self.tarefa.getPrioridade()]['id']
        if idPrioridade < 3:
            idPrioridade+=1
        else:
            idPrioridade = 1

        self.tarefa.setPrioridade(PRIORIDADES_ID[idPrioridade])
        self.checarPrioridade()
    def alterarStatus(self):
        self.tarefa.setStatus(self.vStatus.get())

