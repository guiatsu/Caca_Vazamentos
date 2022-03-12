import re
import sqlite3
from flask import Flask, render_template, url_for, request,redirect,session,flash, g, \
    abort, flash
from models import *

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

@app.route("/database.html")
def show_db():
    return render_template("database.html")

db.create_tables([Pessoa,Endereco,Sensor,Leitura,Denuncia])
app.run(debug=True)