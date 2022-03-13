import cProfile
from typing import Text
from peewee import SqliteDatabase, Model,TextField, ForeignKeyField, DateTimeField, IntegerField

db = SqliteDatabase('caca_vazamentos.db')

class BaseModel(Model):
    class Meta:
        database = db

class Pessoa(BaseModel):
    cpf = TextField(unique = True)
    email = TextField(unique = True)
    senha = TextField()
    creditos = IntegerField(default = 0)
    def Create(cpf,email,senha,creditos):
        Pessoa.create(cpf = cpf, email = email, senha = senha, creditos = creditos)

class Endereco(BaseModel):
    cep = TextField()
    rua = TextField()
    num = TextField()
    def Create(cep,rua,num):
        Endereco.create(cep = cep, rua = rua, num = num)

class Sensor(BaseModel):
    fk_endereco = ForeignKeyField(Endereco, backref = 'endereco')
    def Create(endereco):
        Pessoa.create(fk_endereco = endereco)

        
class Leitura(BaseModel):
    consumo = IntegerField()
    data_leitura = DateTimeField()
    fk_sensor = ForeignKeyField(Sensor, backref = 'sensor')
    def Create(consumo,data_leitura,fk_sensor):
            Pessoa.create(consumo = consumo, data_leitura = data_leitura, fk_sensor = fk_sensor)
    
class Denuncia(BaseModel):
    fk_pessoa = ForeignKeyField(Pessoa, backref = 'pessoa', null=True)
    fk_endereco = ForeignKeyField(Endereco, backref ='endereco')
    descricao = TextField()
    def Create(fk_pessoa,fk_endereco,descricao):
        Pessoa.create(fk_pessoa = fk_pessoa, fk_endereco = fk_endereco, descricao = descricao)

class Alerta_Sensor(BaseModel):
    fk_leitura = ForeignKeyField(Leitura, backref='leituras')
