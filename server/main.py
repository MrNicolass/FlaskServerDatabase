from flask import Flask, flash, redirect, render_template, request, url_for
import database.dbconnection as dbc

#Variável/instância para acessar o Flask de forma mais fácil
app = Flask(__name__, template_folder='Pages')

if __name__ == "__main__":
    #Cria o contexto da aplicação
    app.app_context().push()
    #Inicia o servidor em modo debug
    app.run(debug=True, host="0.0.0.0", port=5000)