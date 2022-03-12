import sqlite3
from flask import Flask, render_template, url_for, request,redirect,session,flash, g
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


if __name__ == "__main__":
    app.run(debug=True)
    