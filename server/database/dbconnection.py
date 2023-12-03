import mysql.connector
from main import flash

def connection():
    #Define a conexão do banco de dados
    cnx = mysql.connector.connect(
        host="localhost",
        port="3306",
        user="root",
        password="MtMsH@+6XDZi",
        database='n3'
    )
    return cnx

def insert(table, *args):
    #Abre a conexão com o banco de dados
    cnx = connection()

    if(table == "usuarios"):
        #Tenta realizar operação de inserção de um novo usuário
        try:
            #Define uma variável para facilicar a utilização do cursor de banco de dados
            with cnx.cursor() as cursor:
                insert = f"INSERT INTO {table} (email, nome, sobrenome, ativo) VALUES (%s, %s, %s, %s)"
                values = args
                cursor.execute(insert, values)

                #Realiza operação de gravar os dados na tabela
                cnx.commit()
                flash("Usuário cadastrado com sucesso!", "Sucesso")

        #Caso não consiga inserir no banco, pega e exibe mensagem de erro que o banco retornar
        except mysql.connector.Error as error:
            flash(f"Falha ao inserir dados! Erro: {error}", "Erro")

        #Após a função ser executada, encerra a conexão com o banco
        finally:
            if connection().is_connected():
                cnx.close()

def select():
    cnx = connection()

    try:
        with cnx.cursor() as cursor:
            cursor.execute("select * from usuarios")
            result = cursor.fetchall()
        
            return result

    except mysql.connector.Error as error:
        flash(f"Falha ao consultar dados! Erro: {error}", "Erro")

    #Após a função ser executada, encerra a conexão com o banco
    finally:
        if connection().is_connected():
            cnx.close()