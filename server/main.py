from flask import Flask, flash, redirect, render_template, request, url_for
import database.dbconnection as dbc
import ujson #Biblioteca "estilziada" para trabalhar com dados em JSON
import os

#Variável para salvar caminho padrão dos arquivos principáis
template_dir = os.path.abspath('client/src/pages')
#Variável/instância para acessar o Flask de forma mais fácil
app = Flask(__name__, template_folder=template_dir)
app.config["SECRET_KEY"] = "random string"

@app.route("/")
def index():
    return render_template("index.html")

#-----<Rotas Usuário>-----

@app.route("/showUsers")
def showUsers():
    if request.method == "GET":
        return render_template("users/showUsers.html", users=dbc.select("usuarios"))
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
        return render_template("users/updateUsers.html", user=dbc.upSelect("usuarios", id))
    return render_template("users/updateUsers.html")

@app.route("/deleteUser/<int:id>", methods=["GET", "POST"])
def deleteUser(id):
    dbc.delete("usuarios", id)
    return redirect(url_for("showUsers"))

#-----</Rotas Usuário>-----

#-----<Rotas Produtos>-----

@app.route("/showProducts")
def showProducts():
    if request.method == "GET":
        return render_template("products/showProducts.html", products=dbc.select("produtos"))
    else:
        return render_template("products/showProducts.html")
    
@app.route("/newProduct", methods=['GET', 'POST'])
def newProduct():
    if request.method == 'POST':
        if not request.form['cod_barras'] or not request.form['descricao'] or not request.form['status'] or not request.form['preco'] or not request.form['precoD'] or not request.form['quantidade']:
            flash("Preencha todos os campos!", "Erro")
        else:
            cod_barras = request.form['cod_barras']
            descricao = request.form['descricao']
            status = int(request.form['status'])
            preco = float(request.form['preco'])
            precoD = float(request.form['precoD'])
            quantidade = int(request.form['quantidade'])
            dbc.insert("produtos", cod_barras, descricao, status, preco, precoD, quantidade)
    return render_template("products/newProduct.html", status=dbc.select("status_produtos"))

@app.route("/updateProduct/<int:id>", methods=['GET', 'POST'])
def updateProduct(id):
    if request.method == 'POST':
        if not request.form['cod_barras'] or not request.form['descricao'] or not request.form['status'] or not request.form['preco'] or not request.form['precoD'] or not request.form['quantidade']:
            flash("Preencha todos os campos!", "Erro")
        else:
            cod_barras = request.form['cod_barras']
            descricao = request.form['descricao']
            status = int(request.form['status'])
            preco = float(request.form['preco'])
            precoD = float(request.form['precoD'])
            quantidade = int(request.form['quantidade'])
            flash(dbc.update("produtos", id, cod_barras, descricao, status, preco, precoD, quantidade))
            #Volta para página principal
            return redirect(url_for("showProducts"))
    else:
        return render_template("products/updateProduct.html", product=dbc.upSelect("produtos", id), status=dbc.select("status_produtos"))
    return render_template("products/updateProduct.html")

@app.route("/deleteProduct/<int:id>", methods=['GET', 'POST'])
def deleteProduct(id):
    dbc.delete("produtos", id)
    return redirect(url_for("showProducts"))

#-----</Rotas Produtos>-----

#-----<Rotas Categorias>-----

@app.route("/showCategories")
def showCategories():
    if request.method == "GET":
        return render_template("categories/showCategories.html", category=dbc.select("categorias"))
    else:
        return render_template("categories/showCategories.html")

@app.route("/newCategory", methods=['GET', 'POST'])
def newCategory():
    if request.method == 'POST':
        if not request.form['nome'] or not request.form['cod_pai']:
            flash("Preencha todos os campos!", "Erro")
        else:
            nome = request.form['nome']
            cod_pai = request.form['cod_pai']
            dbc.insert("categorias", nome, cod_pai)
    return render_template("categories/newCategory.html", category=dbc.select("categorias"))

@app.route("/updateCategory/<int:id>", methods=['GET', 'POST'])
def updateCategory(id):
    if request.method == 'POST':
        if not request.form['nome'] or not request.form['cod_pai']:
            flash("Preencha todos os campos!", "Erro")
        else:
            nome = request.form['nome']
            cod_pai = request.form['cod_pai']
            flash(dbc.update("categorias", id, nome, cod_pai))
            #Volta para página principal
            return redirect(url_for("showCategories"))
    else:
        return render_template("categories/updateCategory.html", category=dbc.upSelect("categorias", id), categ=dbc.select("categorias"))
    return render_template("categories/updateCategory.html")

@app.route("/deleteCategory/<int:id>", methods=['GET', 'POST'])
def deleteCategory(id):
    dbc.delete("categorias", id)
    return redirect(url_for("showCategories"))

#-----</Rotas Categorias>-----

#-----<Rotas RESTful>-----

@app.route("/productListTag")
def productListTag():
    success_json = ujson.dumps(dbc.productListTag())
    return success_json

@app.route("/userBuys/<int:id>")
def userBuys(id):
    success_json = ujson.dumps(dbc.userBuys(id))
    return success_json

@app.route("/productListPerTag/<int:id>")
def productListPerTag(id):
    success_json = ujson.dumps(dbc.productListPerTag(id))
    return success_json

@app.route("/selectURL/<table>")
def selectURL(table):
    return dbc.selectURL(table)

#-----</Rotas RESTful>-----

if __name__ == "__main__":
    #Cria o contexto da aplicação
    app.app_context().push()
    #Inicia o servidor em modo debug
    app.run(debug=True, host="0.0.0.0", port=5000)