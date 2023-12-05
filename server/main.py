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

@app.route("/showUsers")
def showUsers():
    if request.method == "GET":
        return render_template("users/showUsers.html", users=dbc.select())
    else:
        return render_template("users/showUsers.html")

@app.route("/newUsers", methods=['GET', 'POST'])
def newUsers():
    if request.method == 'POST':
        if not request.form['email'] or not request.form['nome'] or not request.form['sobrenome'] or not request.form['ativo']:
            flash("Preencha todos os campos!", "Erro")
        else:
            email = request.form['email']
            nome = request.form['nome']
            sobrenome = request.form['sobrenome']
            ativo = int(request.form['ativo'])
            dbc.insert("usuarios", email, nome, sobrenome, ativo)
    return render_template("users/newUsers.html")

@app.route("/updateUser/<int:id>", methods=["GET", "POST"])
def updateUser(id):
    if request.method == 'POST':
        if not request.form['email'] or not request.form['nome'] or not request.form['sobrenome'] or not request.form['ativo']:
            flash("Preencha todos os campos!", "Erro")
        else:
            email = request.form['email']
            nome = request.form['nome']
            sobrenome = request.form['sobrenome']
            ativo = int(request.form['ativo'])
            flash(dbc.update("usuarios", id, email, nome, sobrenome, ativo))
            #Volta para página principal
            return redirect(url_for("showUsers"))
    else:
        return render_template("users/updateUsers.html", user=dbc.upSelect(id))
    return render_template("users/updateUsers.html")

@app.route("/deleteUser/<int:id>", methods=["GET", "POST"])
def deleteUser(id):
    dbc.delete("usuarios", id)
    return redirect(url_for("showUsers"))

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