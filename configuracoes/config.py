from models.TarefaModel import TarefaModel
from models.StatusModel import StatusModel
from models.PrioridadeModel import PrioridadeModel
from models.Conexao import db

def criarTabelas():
    db.connect()
    db.create_tables([PrioridadeModel, StatusModel, TarefaModel])
    inicializarDados()

def inicializarDados():
    PRIORIDADES = ['Baixa', 'Media', 'Alta']
    STATUS = ['Pendente', 'Concluida']

    if not PrioridadeModel.select().execute() and not StatusModel.select().execute():
        for p in PRIORIDADES:
            PrioridadeModel.create(nomePrioridade=p)
        for s in STATUS:
            StatusModel.create(nomeStatus = s)

criarTabelas()