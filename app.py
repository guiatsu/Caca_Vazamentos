import re
import sqlite3
from flask import Flask, render_template, url_for, request,redirect,session,flash, g, \
    abort, flash
from models import *
from controller import *
from analysis import *

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")


@app.route("/user/<user_name>")
def user(user_name):
    return render_template("user.html", user_name = user_name)
    

@app.route("/teste")
def teste():
    return render_template("teste.html")



@app.route("/database")
def databaseshow():

    pessoas = [p for p in Pessoa.select()]
    denuncias = [d for d in Denuncia.select()]
    enderecos = [e for e in Endereco.select()]
    leituras = [l for l in Leitura.select()]
    sensores = [s for s in Sensor.select()]
    alertas_sensores = [a for a in Alerta_Sensor.select()]

    return render_template("database.html", pessoas=pessoas, denuncias = denuncias, enderecos=enderecos, leituras=leituras, sensores=sensores, alertas_sensores = alertas_sensores)
    

@app.route("/forms", methods=["POST","GET"])
def forms():
    if request.method == "POST":
        cep = request.form["cep"]
        num = request.form["numero"]
        rua = request.form["rua"]
        descricao = request.form["description"]
        
        if len(Endereco.select().where((Endereco.cep == cep) & (Endereco.num == num) & (Endereco.rua == rua))) == 0:
            Endereco.Create(cep, rua, num)
        
        endereco = Endereco.select().where((Endereco.cep == cep) & (Endereco.num == num) & (Endereco.rua == rua))
        
        pessoa = Pessoa.select().where(Pessoa.cpf == '12345678920') 

        post_denuncia(endereco, pessoa , descricao)
                            
        return render_template("forms.html")

    else:
        
        return render_template("forms.html")
@app.route("/forms1", methods=["POST","GET"])
def forms1():
    return render_template("forms.html")
    
@app.route("/report", methods=["POST","GET"])
def report():
    return render_template("report.html")

if __name__ == "__main__":

    # db.create_tables([Pessoa,Endereco,Sensor,Leitura,Denuncia,Alerta_Sensor])
    main()



    # INSERCOES DO BD ABAIXO:
    {
    # pessoas = [
    #     {"cpf":"12345678900", "email": "p1@email.com", "senha": "123456"},
    #     {"cpf":"36600036600", "email": "p2@email.com", "senha": "123456"},
    #     {"cpf":"11100011100", "email": "p3@email.com", "senha": "123456"},
    #     {"cpf":"22200022200", "email": "p4@email.com", "senha": "123456"},
    #     {"cpf":"33300033300", "email": "p5@email.com", "senha": "123456"},
    #     {"cpf":"44400044400", "email": "p6@email.com", "senha": "123456"},
    #     {"cpf":"55500055500", "email": "p7@email.com", "senha": "123456"},
    #     {"cpf":"66600066600", "email": "p8@email.com", "senha": "123456"},
    #     {"cpf":"77700077700", "email": "p9@email.com", "senha": "123456"},
    #     {"cpf":"88800088800", "email": "jose@email.com", "senha": "123456"},
    #     {"cpf":"99900099900", "email": "fulano@email.com", "senha": "123456"},
    #     {"cpf":"14509877700", "email": "p11@email.com", "senha": "123456"},
    # ]

    # enderecos = [

    #     {"cep":"123456-00", "rua":"Rua do Povo", "num": "1"},
    #     {"cep":"123456-00", "rua":"Rua do Povo", "num": "2"},
    #     {"cep":"123456-00", "rua":"Rua do Povo", "num": "3"},
    #     {"cep":"123456-00", "rua":"Rua do Povo", "num": "4"},
    #     {"cep":"123456-00", "rua":"Rua do Povo", "num": "5"},
    #     {"cep":"123456-00", "rua":"Rua do Povo", "num": "6"},
    #     {"cep":"123456-00", "rua":"Rua do Povo", "num": "7"},
    #     {"cep":"123456-00", "rua":"Rua do Povo", "num": "8"},
    #     {"cep":"123456-00", "rua":"Rua do Povo", "num": "9"},
    #     {"cep":"123456-00", "rua":"Rua do Povo", "num": "10"},
    #     {"cep":"123456-00", "rua":"Rua do Povo", "num": "11"},
    #     {"cep":"123456-00", "rua":"Rua do Povo", "num": "12"},
    # ]

    # sensores = [

    #     {"fk_endereco":1},
    #     {"fk_endereco":2},
    #     {"fk_endereco":3},
    #     {"fk_endereco":4},
    #     {"fk_endereco":5},
    # ]


    # leituras1 = [
    #     {'consumo': 2703.70, 'data_leitura': '1/01/2022', 'fk_sensor': 1},
    #     {'consumo': 2856.60, 'data_leitura': '1/02/2022', 'fk_sensor': 1},
    #     {'consumo': 2918.25, 'data_leitura': '1/03/2022', 'fk_sensor': 1},
    #     {'consumo': 3386.73, 'data_leitura': '1/04/2022', 'fk_sensor': 1},
    #     {'consumo': 3019.35, 'data_leitura': '1/05/2022', 'fk_sensor': 1},
    #     {'consumo': 2622.36, 'data_leitura': '1/06/2022', 'fk_sensor': 1},
    #     {'consumo': 3183.96, 'data_leitura': '1/07/2022', 'fk_sensor': 1},
    #     {'consumo': 4505.37, 'data_leitura': '1/08/2022', 'fk_sensor': 1},
    #     {'consumo': 3318.93, 'data_leitura': '1/09/2022', 'fk_sensor': 1},
    #     {'consumo': 2796.51, 'data_leitura': '1/10/2022', 'fk_sensor': 1},
    #     {'consumo': 2923.08, 'data_leitura': '1/11/2022', 'fk_sensor': 1},
    #     {'consumo': 2985.51, 'data_leitura': '1/12/2022', 'fk_sensor': 1},
    # ]

    # # NORMAL
    # leituras2 = [
    #     {'consumo': 1600.0  , 'data_leitura': '1/01/2022', 'fk_sensor': 2},
    #     {'consumo': 1670.0  , 'data_leitura': '1/02/2022', 'fk_sensor': 2},
    #     {'consumo': 1720.0  , 'data_leitura': '1/03/2022', 'fk_sensor': 2},

    #     {'consumo': 1680.0  , 'data_leitura': '1/04/2022', 'fk_sensor': 2},
    #     {'consumo': 1600.0  , 'data_leitura': '1/05/2022', 'fk_sensor': 2},
    #     {'consumo': 1650.0  , 'data_leitura': '1/06/2022', 'fk_sensor': 2},

    #     {'consumo': 1782.0  , 'data_leitura': '1/07/2022', 'fk_sensor': 2},
    #     {'consumo': 1700.0  , 'data_leitura': '1/08/2022', 'fk_sensor': 2},
    #     {'consumo': 1690.0  , 'data_leitura': '1/09/2022', 'fk_sensor': 2},

    #     {'consumo': 1590.0  , 'data_leitura': '1/10/2022', 'fk_sensor': 2},
    #     {'consumo': 1693.0  , 'data_leitura': '1/11/2022', 'fk_sensor': 2},
    #     {'consumo': 1656.0  , 'data_leitura': '1/12/2022', 'fk_sensor': 2},
    # ]

    # #DEVE ACUSAR ERRO
    # leituras3 = [
    #     {'consumo': 1500.0  , 'data_leitura': '1/01/2022', 'fk_sensor': 3},
    #     {'consumo': 1600.0  , 'data_leitura': '1/02/2022', 'fk_sensor': 3},
    #     {'consumo': 1580.0  , 'data_leitura': '1/03/2022', 'fk_sensor': 3},

    #     {'consumo': 1700.0  , 'data_leitura': '1/04/2022', 'fk_sensor': 3},
    #     {'consumo': 1690.0  , 'data_leitura': '1/05/2022', 'fk_sensor': 3},
    #     {'consumo': 1600.0  , 'data_leitura': '1/06/2022', 'fk_sensor': 3},

    #     {'consumo': 1599.0  , 'data_leitura': '1/07/2022', 'fk_sensor': 3},
    #     {'consumo': 1640.0  , 'data_leitura': '1/08/2022', 'fk_sensor': 3},
    #     {'consumo': 1670.0  , 'data_leitura': '1/09/2022', 'fk_sensor': 3},

    #     {'consumo': 3000.0  , 'data_leitura': '1/10/2022', 'fk_sensor': 3},
    #     {'consumo': 2980.0  , 'data_leitura': '1/11/2022', 'fk_sensor': 3},
    #     {'consumo': 2700.0  , 'data_leitura': '1/12/2022', 'fk_sensor': 3},
    # ]

    # #NORMAL
    # leituras4 = [
    #     {'consumo': 2000.0  , 'data_leitura': '1/01/2022', 'fk_sensor': 4},
    #     {'consumo': 1900.0  , 'data_leitura': '1/02/2022', 'fk_sensor': 4},
    #     {'consumo': 2000.0  , 'data_leitura': '1/03/2022', 'fk_sensor': 4},

    #     {'consumo': 1990.0  , 'data_leitura': '1/04/2022', 'fk_sensor': 4},
    #     {'consumo': 1800.0  , 'data_leitura': '1/05/2022', 'fk_sensor': 4},
    #     {'consumo': 10.0     , 'data_leitura': '1/06/2022', 'fk_sensor': 4},

    #     {'consumo': 10.0  , 'data_leitura': '1/07/2022', 'fk_sensor': 4},
    #     {'consumo': 10.0  , 'data_leitura': '1/08/2022', 'fk_sensor': 4},
    #     {'consumo': 10.0  , 'data_leitura': '1/09/2022', 'fk_sensor': 4},

    #     {'consumo': 1600.0  , 'data_leitura': '1/10/2022', 'fk_sensor': 4},
    #     {'consumo': 1700.0  , 'data_leitura': '1/11/2022', 'fk_sensor': 4},
    #     {'consumo': 1650.0  , 'data_leitura': '1/12/2022', 'fk_sensor': 4},
    # ]
    
    # #DEVE APRESENTAR ERRO
    # leituras5 = [
    #     {'consumo': 1500.0  , 'data_leitura': '1/01/2022', 'fk_sensor': 5},
    #     {'consumo': 1500.0  , 'data_leitura': '1/02/2022', 'fk_sensor': 5},
    #     {'consumo': 1500.0  , 'data_leitura': '1/03/2022', 'fk_sensor': 5},

    #     {'consumo': 4000.0  , 'data_leitura': '1/04/2022', 'fk_sensor': 5},
    #     {'consumo': 3500.0  , 'data_leitura': '1/05/2022', 'fk_sensor': 5},
    #     {'consumo': 1500.0  , 'data_leitura': '1/06/2022', 'fk_sensor': 5},

    #     {'consumo': 1500.0  , 'data_leitura': '1/07/2022', 'fk_sensor': 5},
    #     {'consumo': 1500.0  , 'data_leitura': '1/08/2022', 'fk_sensor': 5},
    #     {'consumo': 1500.0  , 'data_leitura': '1/09/2022', 'fk_sensor': 5},

    #     {'consumo': 1500.0  , 'data_leitura': '1/10/2022', 'fk_sensor': 5},
    #     {'consumo': 1500.0  , 'data_leitura': '1/11/2022', 'fk_sensor': 5},
    #     {'consumo': 1500.0  , 'data_leitura': '1/12/2022', 'fk_sensor': 5},
    # ]
    # Pessoa.insert_many(pessoas).execute()
    # Endereco.insert_many(enderecos).execute()
    # Sensor.insert_many(sensores).execute()
    # Leitura.insert_many(leituras1).execute()
    # Leitura.insert_many(leituras2).execute()
    # Leitura.insert_many(leituras3).execute()
    # Leitura.insert_many(leituras4).execute()
    # Leitura.insert_many(leituras5).execute()
#     denuncias = [

#         {},
#         {},
#         {},
#         {},
#         {},
#         {},
#         {},
#         {},
#         {},
#         {},
#         {},
#         {},
#     ]
    }
    
    app.run(debug=True)

