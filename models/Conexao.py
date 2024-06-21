from peewee import SqliteDatabase, Model

db = SqliteDatabase('tarefadb.db')
class DataModel(Model):
    class Meta:
        database = db