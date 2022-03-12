import cProfile
from typing import Text
from peewee import SqliteDatabase, Model,TextField, ForeignKeyField, DateTimeField, IntegerField

db = SqliteDatabase('caca_vazamentos.db')


class BaseModel(Model):
    class Meta:
        database = db

class Pessoa(BaseModel):
    cpf = TextField(unique=True)
    email = TextField(unique=True)
    senha = TextField()
    creditos = IntegerField()

class Endereco(BaseModel):
    cep = TextField()
    num = TextField()


class Sensor(BaseModel):
    id = TextField()
    fk_endereco = ForeignKeyField(Endereco, backref = 'endereco')
        
class Leitura(BaseModel):
    consumo = IntegerField()
    data_leitura = DateTimeField()
    fk_sensor = ForeignKeyField(Sensor, backref = 'sensor')
class Denuncia(BaseModel):
    fk_leitura = ForeignKeyField(Leitura, backref = 'leitura')
    
######################################################

# from peewee import *
# from flask_peewee.db import Database
# from flask_peewee.admin import Admin
# from flask_peewee.auth import Auth,BaseUser

# DATABASE = {
#     'name': 'denuncias_vazamento',
#     'engine': 'peewee.SqliteDatabase',
# }
# auth = Auth(app,db)
# admin = Admin(app,auth)
# from app.py import app

# db = peewee.SqliteDatabase('denuncias_vazamento.db')
# class BaseModel(Model):
#     class Meta:
#         database = db

# class User(db.Model,BaseUser):
#     cpf = CharField()
#     password = CharField()
#     is_superuser = BooleanField()

