from models import *

def post_denuncia(endereco, pessoa, descricao, tipo_vazamento, status):

    
    Denuncia.create(fk_endereco=endereco,fk_pessoa=pessoa, descricao=descricao, tipo_vazamento=tipo_vazamento, status=status)

    return

def insert_pessoas():
    
    pessoas = [
        {"cpf":"12345678900", "nome": "Administrador" , "email": "p1@email.com", "senha": "123456"},
        {"cpf":"36600036600", "nome": "testolho2" , "email": "p2@email.com", "senha": "123456"},
        {"cpf":"11100011100", "nome": "testolho3" , "email": "p3@email.com", "senha": "123456"},
        {"cpf":"22200022200", "nome": "testolho4" , "email": "p4@email.com", "senha": "123456"},
        {"cpf":"33300033300", "nome": "testolho5" , "email": "p5@email.com", "senha": "123456"},
        {"cpf":"44400044400", "nome": "testolho6" , "email": "p6@email.com", "senha": "123456"},
        {"cpf":"55500055500", "nome": "testolho7" , "email": "p7@email.com", "senha": "123456"},
        {"cpf":"66600066600", "nome": "testolho8" , "email": "p8@email.com", "senha": "123456"},
        {"cpf":"77700077700", "nome": "testolho9" , "email": "p9@email.com", "senha": "123456"},
        {"cpf":"88800088800", "nome": "Cléber" , "email": "jose@email.com", "senha": "123456"},
        {"cpf":"99900099900", "nome": "Cletinho" , "email": "fulano@email.com", "senha": "123456"},
        {"cpf":"14509877700", "nome": "testolho12" , "email": "p11@email.com", "senha": "123456"},
    ]
    Pessoa.insert_many(pessoas).execute()

def insert_enderecos():
    enderecos = [

        {"cep":"123456-00", "rua":"Rua do Povo", "num": "1"},
        {"cep":"123456-00", "rua":"Rua do Povo", "num": "2"},
        {"cep":"123456-00", "rua":"Rua do Povo", "num": "3"},
        {"cep":"123456-00", "rua":"Rua do Povo", "num": "4"},
        {"cep":"123456-00", "rua":"Rua do Povo", "num": "5"},
        {"cep":"123456-00", "rua":"Rua do Povo", "num": "6"},
        {"cep":"123456-00", "rua":"Rua do Povo", "num": "7"},
        {"cep":"123456-00", "rua":"Rua do Povo", "num": "8"},
        {"cep":"123456-00", "rua":"Rua do Povo", "num": "9"},
        {"cep":"123456-00", "rua":"Rua do Povo", "num": "10"},
        {"cep":"123456-00", "rua":"Rua do Povo", "num": "11"},
        {"cep":"123456-00", "rua":"Rua do Povo", "num": "12"},
    ]

    Endereco.insert_many(enderecos).execute()

def insert_sensores():

    sensores = [

        {"fk_endereco":1},
        {"fk_endereco":2},
        {"fk_endereco":3},
        {"fk_endereco":4},
        {"fk_endereco":5},
    ]

    Sensor.insert_many(sensores).execute()

def insert_leituras():

    #Acusa erro
    leituras1 = [
        {'consumo': 2703.70, 'data_leitura': '1/01/2022', 'fk_sensor': 1},
        {'consumo': 2856.60, 'data_leitura': '1/02/2022', 'fk_sensor': 1},
        {'consumo': 2918.25, 'data_leitura': '1/03/2022', 'fk_sensor': 1},

        {'consumo': 3386.73, 'data_leitura': '1/04/2022', 'fk_sensor': 1},
        {'consumo': 3019.35, 'data_leitura': '1/05/2022', 'fk_sensor': 1},
        {'consumo': 2622.36, 'data_leitura': '1/06/2022', 'fk_sensor': 1},

        {'consumo': 3183.96, 'data_leitura': '1/07/2022', 'fk_sensor': 1},
        {'consumo': 4505.37, 'data_leitura': '1/08/2022', 'fk_sensor': 1},
        {'consumo': 3318.93, 'data_leitura': '1/09/2022', 'fk_sensor': 1},
        
        {'consumo': 2796.51, 'data_leitura': '1/10/2022', 'fk_sensor': 1},
        {'consumo': 2923.08, 'data_leitura': '1/11/2022', 'fk_sensor': 1},
        {'consumo': 2985.51, 'data_leitura': '1/12/2022', 'fk_sensor': 1},
    ]

    # NORMAL
    leituras2 = [
        {'consumo': 1600.0  , 'data_leitura': '1/01/2022', 'fk_sensor': 2},
        {'consumo': 1670.0  , 'data_leitura': '1/02/2022', 'fk_sensor': 2},
        {'consumo': 1720.0  , 'data_leitura': '1/03/2022', 'fk_sensor': 2},

        {'consumo': 1680.0  , 'data_leitura': '1/04/2022', 'fk_sensor': 2},
        {'consumo': 1600.0  , 'data_leitura': '1/05/2022', 'fk_sensor': 2},
        {'consumo': 1650.0  , 'data_leitura': '1/06/2022', 'fk_sensor': 2},

        {'consumo': 1782.0  , 'data_leitura': '1/07/2022', 'fk_sensor': 2},
        {'consumo': 1700.0  , 'data_leitura': '1/08/2022', 'fk_sensor': 2},
        {'consumo': 1690.0  , 'data_leitura': '1/09/2022', 'fk_sensor': 2},

        {'consumo': 1590.0  , 'data_leitura': '1/10/2022', 'fk_sensor': 2},
        {'consumo': 1693.0  , 'data_leitura': '1/11/2022', 'fk_sensor': 2},
        {'consumo': 1656.0  , 'data_leitura': '1/12/2022', 'fk_sensor': 2},
    ]

    #DEVE ACUSAR ERRO
    leituras3 = [
        {'consumo': 1500.0  , 'data_leitura': '1/01/2022', 'fk_sensor': 3},
        {'consumo': 1600.0  , 'data_leitura': '1/02/2022', 'fk_sensor': 3},
        {'consumo': 1580.0  , 'data_leitura': '1/03/2022', 'fk_sensor': 3},

        {'consumo': 1700.0  , 'data_leitura': '1/04/2022', 'fk_sensor': 3},
        {'consumo': 1690.0  , 'data_leitura': '1/05/2022', 'fk_sensor': 3},
        {'consumo': 1600.0  , 'data_leitura': '1/06/2022', 'fk_sensor': 3},

        {'consumo': 1599.0  , 'data_leitura': '1/07/2022', 'fk_sensor': 3},
        {'consumo': 1640.0  , 'data_leitura': '1/08/2022', 'fk_sensor': 3},
        {'consumo': 1670.0  , 'data_leitura': '1/09/2022', 'fk_sensor': 3},

        {'consumo': 3000.0  , 'data_leitura': '1/10/2022', 'fk_sensor': 3},
        {'consumo': 2980.0  , 'data_leitura': '1/11/2022', 'fk_sensor': 3},
        {'consumo': 2700.0  , 'data_leitura': '1/12/2022', 'fk_sensor': 3},
    ]

    #NORMAL
    leituras4 = [
        {'consumo': 2000.0  , 'data_leitura': '1/01/2022', 'fk_sensor': 4},
        {'consumo': 1900.0  , 'data_leitura': '1/02/2022', 'fk_sensor': 4},
        {'consumo': 2000.0  , 'data_leitura': '1/03/2022', 'fk_sensor': 4},

        {'consumo': 1990.0  , 'data_leitura': '1/04/2022', 'fk_sensor': 4},
        {'consumo': 1800.0  , 'data_leitura': '1/05/2022', 'fk_sensor': 4},
        {'consumo': 10.0     , 'data_leitura': '1/06/2022', 'fk_sensor': 4},

        {'consumo': 10.0  , 'data_leitura': '1/07/2022', 'fk_sensor': 4},
        {'consumo': 10.0  , 'data_leitura': '1/08/2022', 'fk_sensor': 4},
        {'consumo': 10.0  , 'data_leitura': '1/09/2022', 'fk_sensor': 4},

        {'consumo': 1600.0  , 'data_leitura': '1/10/2022', 'fk_sensor': 4},
        {'consumo': 1700.0  , 'data_leitura': '1/11/2022', 'fk_sensor': 4},
        {'consumo': 1650.0  , 'data_leitura': '1/12/2022', 'fk_sensor': 4},
    ]
    
    #DEVE APRESENTAR ERRO
    leituras5 = [
        {'consumo': 1500.0  , 'data_leitura': '1/01/2022', 'fk_sensor': 5},
        {'consumo': 1500.0  , 'data_leitura': '1/02/2022', 'fk_sensor': 5},
        {'consumo': 1500.0  , 'data_leitura': '1/03/2022', 'fk_sensor': 5},

        {'consumo': 4000.0  , 'data_leitura': '1/04/2022', 'fk_sensor': 5},
        {'consumo': 3500.0  , 'data_leitura': '1/05/2022', 'fk_sensor': 5},
        {'consumo': 1500.0  , 'data_leitura': '1/06/2022', 'fk_sensor': 5},

        {'consumo': 1500.0  , 'data_leitura': '1/07/2022', 'fk_sensor': 5},
        {'consumo': 1500.0  , 'data_leitura': '1/08/2022', 'fk_sensor': 5},
        {'consumo': 1500.0  , 'data_leitura': '1/09/2022', 'fk_sensor': 5},

        {'consumo': 1500.0  , 'data_leitura': '1/10/2022', 'fk_sensor': 5},
        {'consumo': 1500.0  , 'data_leitura': '1/11/2022', 'fk_sensor': 5},
        {'consumo': 1500.0  , 'data_leitura': '1/12/2022', 'fk_sensor': 5},
    ]
    Leitura.insert_many(leituras1).execute()
    Leitura.insert_many(leituras2).execute()
    Leitura.insert_many(leituras3).execute()
    Leitura.insert_many(leituras4).execute()
    Leitura.insert_many(leituras5).execute()
 
def insert_denuncias():

    denuncias = [

        {},
        {},
        {},
        {},
        {},
        {},
        {},
        {},
        {},
        {},
        {},
        {},
    ]

    return

def reset_db():

    # tables = db.get_tables()
    # print(tables)
    # db.drop_tables([Pessoa, Endereco, Sensor, Leitura, Denuncia, Alerta_Sensor])
    # print(tables)

    db.create_tables([Pessoa,Endereco,Sensor,Leitura,Denuncia,Alerta_Sensor])
    insert_pessoas()
    insert_enderecos()
    insert_sensores()
    insert_leituras()

    return