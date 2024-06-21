from models.TarefaModel import TarefaModel
from models.PrioridadeModel import PrioridadeModel
from models.StatusModel import StatusModel
class Tarefa:
    def __init__(self, idTarefa:int, nomeTarefa:str, prioridadeTarefa:str, dataHoraTarefa:str, statusTarefa:str):
        self.__id = idTarefa
        self.__nome = nomeTarefa
        self.__prioridade = prioridadeTarefa
        self.__dataHora = dataHoraTarefa
        self.__status = statusTarefa

    def getId(self):
        return self.__id
    def getNome(self):
        return self.__nome

    def getPrioridade(self):
        return self.__prioridade

    def getDataHora(self):
        return self.__dataHora

    def getStatus(self):
        return self.__status

    def setNome(self, nomeTarefa:str):
        self.__nome = nomeTarefa

    def setPrioridade(self, prioridadeTarefa:str):
        self.__prioridade = prioridadeTarefa
        tarefa = TarefaModel.get(TarefaModel.id == self.__id)
        if tarefa:
            tarefa.prioridadeTarefa = PrioridadeModel.select(PrioridadeModel.id).where(PrioridadeModel.nomePrioridade == prioridadeTarefa).execute()[0].id
            tarefa.save()

    def setDataHora(self, dataHoraTarefa:str):
        self.__dataHora = dataHoraTarefa

    def setStatus(self, statusTarefa:str):
        self.__status = statusTarefa
        tarefa = TarefaModel.get(TarefaModel.id == self.__id)
        if tarefa:
            tarefa.statusTarefa = StatusModel.select(StatusModel.id).where(StatusModel.nomeStatus == statusTarefa).execute()[0].id
            tarefa.save()

    def excluirTarefa(self):
        tarefa = TarefaModel.get(TarefaModel.id == self.__id)
        tarefa.delete_instance()
