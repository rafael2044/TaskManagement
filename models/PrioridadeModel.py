from models.Conexao import DataModel
from peewee import CharField


class PrioridadeModel(DataModel):
    nomePrioridade = CharField()

