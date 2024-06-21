from models.Conexao import DataModel
from peewee import CharField

class StatusModel(DataModel):
    nomeStatus = CharField()

