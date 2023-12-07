from flask import Flask, flash, redirect, render_template, request, url_for
import database.dbconnection as dbc #Arquivo com a conexão ao banco de dados e suas funções
import ujson #Biblioteca "estilziada" para trabalhar com dados em JSON
import os #Bibliote do sistema operacional -> Utilizada apenas para definir ra rota padrão de páginas

#Variável para salvar caminho padrão dos arquivos principáis (páginas)
template_dir = os.path.abspath('client/src/pages')
#Variável/instância para acessar o Flask de forma mais fácil e definição da pasta padrão de arquivos
app = Flask(__name__, template_folder=template_dir)
#Chave de segurança com codificação de dados
app.config["SECRET_KEY"] = "random string"

#-----<Rotas Padrão>-----

@app.route("/")
def index():
    return render_template("index.html")

#-----<Rotas Usuário>-----

@app.route("/showUsers")
def showUsers():
    #Retorna a renderização da página de apresentação de usuários e envia ao HTML uma lista com os dados de todos usuários
    return render_template("users/showUsers.html", users=dbc.select("usuarios"))

@app.route("/newUsers", methods=['GET', 'POST'])
def newUsers():
    #Caso receba uma requisição POST
    if request.method == 'POST':
        #Verifica se todos os dados foram preenchidos no formulário (ou se estão sendo todos recebidos no geral)
        if not request.form['email'] or not request.form['nome'] or not request.form['sobrenome'] or not request.form['ativo']:
            #Se não tiver recebido todos os campos, apresenta mensagem de erro
            flash("Preencha todos os campos!", "Erro")
        else:
            #Se tudo estiver certo, grava os dados recebidos dos seus devidos inputs e salva em variáveis
            email = request.form['email']
            nome = request.form['nome']
            sobrenome = request.form['sobrenome']
            #Grava o valor recebido do input tipo "radio" e tranforma em um número inteiro
            ativo = int(request.form['ativo'])
            #Executa a função de inserção, passando em qual tabela irá realizar a operação e quais seus parâmetros
            dbc.insert("usuarios", email, nome, sobrenome, ativo)
    #Renderiza a página
    return render_template("users/newUsers.html")

#Rota de update recebe o ID de qual usuário terá seus dados alterados
@app.route("/updateUser/<int:id>", methods=["GET", "POST"])
def updateUser(id):
    #Caso receba uma requisição POST
    if request.method == 'POST':
        #Realiza o mesmo processo de conferência de compos preenchidos ou não
        if not request.form['email'] or not request.form['nome'] or not request.form['sobrenome'] or not request.form['ativo']:
            flash("Preencha todos os campos!", "Erro")
        else:
            email = request.form['email']
            nome = request.form['nome']
            sobrenome = request.form['sobrenome']
            ativo = int(request.form['ativo'])
            #Chama a função de update, passando em qual tabela será realizado a operação, em qual usuário ocorrerá a modificação
            #e seus novos (ou antigos valores caso não seja alterado nada) valores
            #Após isso, a função retorna uma mensagem a ser apresentado na tela por meio da função Flash
            flash(dbc.update("usuarios", id, email, nome, sobrenome, ativo))
            #Redireciona automaticamente para página principal
            return redirect(url_for("showUsers"))
    else:
        #Caso a requisição seja GET, carrega a página de update e passa ao HTML uma lista com os dados do usuário em questão
        return render_template("users/updateUsers.html", user=dbc.upSelect("usuarios", id))
    #Caso não se enquadre em nenhum parâmetro, direciona o usuário para página de criação de usuários
    return render_template("users/newUsers.html")

#Rota recebe o ID do usuário a ser deletado
@app.route("/deleteUser/<int:id>", methods=["GET", "POST"])
def deleteUser(id):
    #Realiza função de delete, passando em qual tabela realizar operação e o ID do usuário a ser deletado
    flash(dbc.delete("usuarios", id))
    #Recarrega página
    return redirect(url_for("showUsers"))

#-----</Rotas Usuário>-----

#-----<Rotas Produtos>-----

@app.route("/showProducts")
def showProducts():
    return render_template("products/showProducts.html", products=dbc.select("produtos"))
    
@app.route("/newProduct", methods=['GET', 'POST'])
def newProduct():
    if request.method == 'POST':
        if not request.form['cod_barras'] or not request.form['descricao'] or not request.form['status'] or not request.form['preco'] or not request.form['precoD'] or not request.form['quantidade']:
            flash("Preencha todos os campos!", "Erro")
        else:
            #Guarda os valores em variáveis
            cod_barras = request.form['cod_barras']
            descricao = request.form['descricao']
            #Transforma os respectivos valores passados na tag Select do HTML em números inteiros
            status = int(request.form['status'])
            #Transforma os números digitados string em números com ponto flutuante e um inteiro
            preco = float(request.form['preco'])
            precoD = float(request.form['precoD'])
            quantidade = int(request.form['quantidade'])
            dbc.insert("produtos", cod_barras, descricao, status, preco, precoD, quantidade)
    #Carrega a página de novos produtos e passa uma lista para o HTML com os dados da tabela de status dos produtos
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
        #Carrega a página de update passando duas lista, a primeira trás os dados do produto a ser alterado
        #e a outra lista os valores da tabela de status dos produtos, para que seja possível selecionar os status cadastrado
        return render_template("products/updateProduct.html", product=dbc.upSelect("produtos", id), status=dbc.select("status_produtos"))
    return render_template("products/updateProduct.html")

@app.route("/deleteProduct/<int:id>", methods=['GET', 'POST'])
def deleteProduct(id):
    flash(dbc.delete("produtos", id))
    return redirect(url_for("showProducts"))

#-----</Rotas Produtos>-----

#-----<Rotas Categorias>-----

@app.route("/showCategories")
def showCategories():
    return render_template("categories/showCategories.html", category=dbc.select("categorias"))

@app.route("/newCategory", methods=['GET', 'POST'])
def newCategory():
    if request.method == 'POST':
        if not request.form['nome'] or not request.form['cod_pai']:
            flash("Preencha todos os campos!", "Erro")
        else:
            nome = request.form['nome']
            cod_pai = request.form['cod_pai']
            dbc.insert("categorias", nome, cod_pai)
    #Carrega a página de nova categoria e trás uma lista das categorias cadstradas na tabela para seleção do novo cadastro
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
        #Carrega a página de update de categorias passando duas listas, uma trazendo os dados da categoria a ser alterada
        #e a outra uma lista das categorias cadastradas para seleção
        return render_template("categories/updateCategory.html", category=dbc.upSelect("categorias", id), categ=dbc.select("categorias"))
    return render_template("categories/updateCategory.html")

@app.route("/deleteCategory/<int:id>", methods=['GET', 'POST'])
def deleteCategory(id):
    flash(dbc.delete("categorias", id))
    return redirect(url_for("showCategories"))

#-----</Rotas Categorias>-----

#-----<Rotas RESTful>-----

#Apresentar a listagem de produtos e suasTAGs.
@app.route("/productListTag")
def productListTag():
    #Chama a função que apresenta os valores do resultado do select da view e logo após transforma os resultados
    #da lista em JSON
    success_json = ujson.dumps(dbc.productListTag())
    #Retorna para a rota e carrega o resultado em JSON
    return success_json

#Apresentar a listagem de compras do usuário, onde recebe o ID do usuário a ser pesquisado.
@app.route("/userBuys/<int:id>")
def userBuys(id):
    #Chama a função que apresenta os valores do resultado do select da view e logo após transforma os resultados
    #da lista em JSON
    success_json = ujson.dumps(dbc.userBuys(id))
    #Retorna para a rota e carrega o resultado em JSON
    return success_json

#Apresentar a listagem de produtos por uma determinada TAG.
@app.route("/productListPerTag/<int:id>")
def productListPerTag(id):
    #Chama a função que apresenta os valores do resultado do select da view e logo após transforma os resultados
    #da lista em JSON
    success_json = ujson.dumps(dbc.productListPerTag(id))
    #Retorna para a rota e carrega o resultado em JSON
    return success_json

#Rota para trazer o select de alguma tabela a ser passada na URL
@app.route("/selectURL/<table>")
def selectURL(table):
    #Retorna o resultado do select
    return dbc.selectURL(table)

#-----</Rotas RESTful>-----

if __name__ == "__main__":
    #Cria o contexto da aplicação
    app.app_context().push()
    #Inicia o servidor em modo debug
    app.run(debug=True, host="0.0.0.0", port=5000)