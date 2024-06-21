from models.TarefaModel import TarefaModel
class Tarefa:
    def __init__(self, idTarefa:int, nomeTarefa:str, prioridadeTarefa:str, dataHoraTarefa:str, statusTarefa:str):
        self.__id = idTarefa
        self.__nome = nomeTarefa
        self.__prioridade = prioridadeTarefa
        self.__dataHora = dataHoraTarefa
        self.__status = statusTarefa

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
            tarefa.prioridadeTarefa = prioridadeTarefa
            tarefa.save()

    def setDataHora(self, dataHoraTarefa:str):
        self.__dataHora = dataHoraTarefa

    def setStatus(self, statusTarefa:str):
        self.__status = statusTarefa
        tarefa = TarefaModel.get(TarefaModel.id == self.__id)
        if tarefa:
            tarefa.statusTarefa = statusTarefa
            tarefa.save()