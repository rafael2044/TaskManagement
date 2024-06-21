from peewee import CharField, ForeignKeyField, DateTimeField
from models.Conexao import DataModel
from models.StatusModel import StatusModel
from models.PrioridadeModel import PrioridadeModel
import datetime

class TarefaModel(DataModel):
    nomeTarefa = CharField()
    prioridadeTarefa = ForeignKeyField(PrioridadeModel, backref='tarefas')
    dataHoraTarefa = DateTimeField(formats="%d/%m/%Y %H:%M",
                                   default=datetime.datetime.now().strftime("%d/%m/%Y %H:%M"))
    statusTarefa = ForeignKeyField(StatusModel, backref='tarefas')
