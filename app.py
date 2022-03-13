import re
import sqlite3
from flask import Flask, render_template, url_for, request,redirect,session,flash, g, \
    abort, flash

from models import *
from controller import *
from analysis import *

app = Flask(__name__)
app.secret_key = 'xablauxoribaluboribau'
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(cpf):
    try:
        return Pessoa.select().where(Pessoa.cpf == cpf).get()
    except Pessoa.DoesNotExist:
        return None

@app.route("/", methods=["POST","GET"])
def homepage():
    if request.method == "POST":
        
        cpf = request.form["cpf"]
        senha = request.form["senha"]

        pessoa = load_user(cpf)

        if(pessoa != None and senha == pessoa.senha):
            login_user(pessoa)
            flash("logado com sucesso")
            return redirect(url_for('user'))
        else:
            return render_template("index.html")

    else:
        if(current_user.is_authenticated):
            return redirect(url_for('user'))
        return render_template("index.html")

@app.route("/cadastrar", methods=["POST","GET"])
def signup():
    if request.method == "POST":
        cpf = request.form["cpf"]
        nome = request.form["nome"]
        email = request.form["email"]
        senha = request.form["senha"]
        confirmar_senha = request.form["confirmar_senha"]
        print(cpf,nome,email,senha,confirmar_senha)
        if(senha != confirmar_senha):
            return render_template("signup.html")
        
        if len(Pessoa.select().where((Pessoa.cpf == cpf) | (Pessoa.email == email))) == 0:
            pessoa = Pessoa(cpf = cpf,nome = nome,email = email,senha = senha)
            if(pessoa != None):
                pessoa.save()
                login_user(pessoa)
                return redirect(url_for('user',user_name = nome))
        else:
            return render_template("signup.html")
                        

    else:

        return render_template("signup.html")

@app.route("/user")
@login_required
def user():
    return render_template("user.html")
    
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('homepage'))

@app.route("/teste")
@login_required
def teste():
    return render_template("teste.html")


@app.route("/database")
def databaseshow():

    pessoas = [p for p in Pessoa.select()]
    denuncias = [d for d in Denuncia.select()]
    enderecos = [e for e in Endereco.select()]
    leituras = [l for l in Leitura.select()]
    sensores = [s for s in Sensor.select()]

    return render_template("database.html", pessoas=pessoas, denuncias = denuncias, enderecos=enderecos, leituras=leituras, sensores=sensores)
    

@app.route("/forms", methods=["POST","GET"])
@login_required
def forms():
    if request.method == "POST":

        cep = request.form["cep"]
        num = request.form["numero"]
        rua = request.form["rua"]
        descricao = request.form["description"]
        tipo_vazamento = request.form["reports"]
        status = "Em analise"
        
        if len(Endereco.select().where((Endereco.cep == cep) & (Endereco.num == num) & (Endereco.rua == rua))) == 0:
            Endereco.Create(cep, rua, num)
        
        endereco = Endereco.select().where((Endereco.cep == cep) & (Endereco.num == num) & (Endereco.rua == rua))
        
        pessoa = Pessoa.select().where(Pessoa.cpf == current_user.get_id()) 

        post_denuncia(endereco, pessoa , descricao, tipo_vazamento, status)
                            
        return render_template("forms.html")

    else:
        
        return render_template("forms.html")

@app.route("/user/admin/alertas")
@login_required
def alertas():

    alertas_sensores = [a for a in Alerta_Sensor.select()]

    return render_template("alertaVazamentos.html", alertas_sensores=alertas_sensores)

@app.route("/forms1", methods=["POST","GET"])
@login_required
def forms1():
    return render_template("forms1.html")
    
@app.route("/report", methods=["POST","GET"])
@login_required
def report():

    denuncias = [d for d in Denuncia.select().where(Denuncia.fk_pessoa == current_user)]

    return render_template("report.html", denuncias=denuncias, len=len(denuncias))

if __name__ == "__main__":
    
    # analysis()

    # reset_db()
    app.run(debug=True)
