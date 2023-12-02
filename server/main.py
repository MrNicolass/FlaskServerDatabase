from flask import Flask, flash, redirect, render_template, request, url_for
import database.dbconnection as dbc
import os

#Variável para salvar caminho padrão dos arquivos principáis
template_dir = os.path.abspath('client/src/pages')
#Variável/instância para acessar o Flask de forma mais fácil
app = Flask(__name__, template_folder=template_dir)
app.config["SECRET_KEY"] = "random string"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/users", methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        if not request.form['email'] or not request.form['nome'] or not request.form['sobrenome'] or not request.form['ativo']:
            flash("Preencha todos os campos", "Erro")
        else:
            email = request.form['email']
            nome = request.form['nome']
            sobrenome = request.form['sobrenome']
            ativo = int(request.form['ativo'])
            dbc.user_insert(email, nome, sobrenome, ativo)
    return render_template("users.html")

@app.route("/products")
def products():
    return render_template("products.html")

@app.route("/categories")
def categories():
    return render_template("categories.html")

if __name__ == "__main__":
    #Cria o contexto da aplicação
    app.app_context().push()
    #Inicia o servidor em modo debug
    app.run(debug=True, host="0.0.0.0", port=5000)