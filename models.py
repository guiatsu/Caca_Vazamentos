import cProfile
from typing import Text
from peewee import SqliteDatabase, Model,TextField, ForeignKeyField, DateTimeField, IntegerField
from flask_login import UserMixin,LoginManager,login_user,login_required,logout_user,current_user

db = SqliteDatabase('caca_vazamentos.db')

class BaseModel(Model):
    class Meta:
        database = db

class Pessoa(BaseModel, UserMixin):
    cpf = TextField(unique = True)
    nome = TextField()
    email = TextField(unique = True)
    senha = TextField()
    creditos = IntegerField(default = 0)
    def Create(cpf,nome,email,senha,creditos):
        Pessoa.create(cpf = cpf,nome = nome,email = email, senha = senha, creditos = creditos)
    def get_id(self):
        return self.cpf
    def get_nome(self):
        return self.nome
    
class Endereco(BaseModel):
    cep = TextField()
    rua = TextField()
    num = TextField()
    def Create(cep,rua,num):
        Endereco.create(cep = cep, rua = rua, num = num)

class Sensor(BaseModel):
    fk_endereco = ForeignKeyField(Endereco, backref = 'endereco')
    def Create(endereco):
        Sensor.create(fk_endereco = endereco)

        
class Leitura(BaseModel):
    consumo = IntegerField()
    data_leitura = DateTimeField()
    fk_sensor = ForeignKeyField(Sensor, backref = 'sensor')
    def Create(consumo,data_leitura,fk_sensor):
            Leitura.create(consumo = consumo, data_leitura = data_leitura, fk_sensor = fk_sensor)
    
class Denuncia(BaseModel):
    fk_pessoa = ForeignKeyField(Pessoa, backref = 'pessoa', null=True)
    fk_endereco = ForeignKeyField(Endereco, backref ='endereco')
    descricao = TextField()
    tipo_vazamento = TextField()
    status = TextField()
    def Create(fk_pessoa,fk_endereco,descricao, tipo, status):
        Denuncia.create(fk_pessoa = fk_pessoa, fk_endereco = fk_endereco, descricao = descricao, tipo_vazamento=tipo, status=status)
    def Get_Denuncias():
        return Denuncia.select()

class Alerta_Sensor(BaseModel):
    fk_leitura = ForeignKeyField(Leitura, backref='leituras')

