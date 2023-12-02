import mysql.connector
from main import flash

def user_insert(email,nome,sobrenome,ativo):
    #Define a conexão do banco de dados
    cnx = mysql.connector.connect(
        host="localhost",
        port="3306",
        user="root",
        password="MtMsH@+6XDZi",
        database='n3'
    )
    
    #Define uma variável para facilicar a utilização do cursos de banco de dados
    dbcursor = cnx.cursor()

    #Tenta realizar operação de inserção de um novo usuário
    try:
        insert = f"INSERT INTO usuarios (email, nome, sobrenome, ativo) VALUES (%s, %s, %s, %s)"
        values = [email, nome, sobrenome, ativo]
        dbcursor.execute(insert, values)

        #Realiza operação de gravar os dados na tabela
        cnx.commit()
        flash("Usuário cadastrado com sucesso!", "Sucesso")

    #Caso não consiga inserir, pega e exibe mensagem de erro do banco de dados
    except mysql.connector.Error as error:
        flash(f"Falha ao inserir dados, erro: {error}", "Erro")

    finally:
        if cnx.is_connected():
            dbcursor.close()
            cnx.close()