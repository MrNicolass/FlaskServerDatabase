import mysql.connector
from main import flash

#Função de conexão ao banco de dados
def connection():
    #Define a conexão do banco de dados
    cnx = mysql.connector.connect(
        host="localhost", #IP de conexão
        port="3306", #Porta de conexão
        user="root", #Usuário do banco/conexão
        password="MtMsH@+6XDZi", #Senha do banco/conexão
        database='n3' #Banco a ser conectado
    )
    #Retorna conexão para ser utilizada em outras funções
    return cnx

#Função de inserção/cadastro nas tabelas, onde recebe a tabela a ser inseridos os dados e os valores (argumentos)
def insert(table, *args):
    #Faz a inserção/cadastro do usuário
    if(table == "usuarios"):
        #Abre a conexão com o banco de dados
        cnx = connection()

        #Tenta realizar operação de inserção de um novo usuário
        try:
            #Define uma variável para facilicar a utilização do cursor de banco de dados
            with cnx.cursor() as cursor:
                #Cria um variável para guardar a query de inserção dos dados na tabela escolhida
                insert = f"INSERT INTO {table} (email, nome, sobrenome, ativo) VALUES (%s, %s, %s, %s)"
                #Executa query realizada anteriormente adicionando os valores que antes estavam como placeholders (%s)
                cursor.execute(insert, args)

                #Realiza efetivamente operação de gravar os dados na tabela
                cnx.commit()
                flash("Usuário cadastrado com sucesso!", "Sucesso")

        #Caso não consiga inserir no banco, pega e exibe mensagem de erro que o banco retornar
        except mysql.connector.Error as error:
            flash(f"Falha ao inserir dados! Erro: {error}", "Erro")

        #Após a função ser executada, encerra a conexão com o banco
        finally:
            if connection().is_connected():
                cnx.close()

    elif(table == "produtos"):
        #Abre a conexão com o banco de dados
        cnx = connection()

        #Tenta realizar operação de inserção de um novo usuário
        try:
            #Define uma variável para facilicar a utilização do cursor de banco de dados
            with cnx.cursor() as cursor:
                insert = f"INSERT INTO {table} (cod_barras, descricao, id_status_produto, preco_normal, preco_com_desconto, quantidade) VALUES (%s, %s, %s, %s, %s, %s)"
                cursor.execute(insert, args)

                #Realiza efetivamente operação de gravar os dados na tabela
                cnx.commit()
                flash("Produto cadastrado com sucesso!", "Sucesso")

        #Caso não consiga inserir no banco, pega e exibe mensagem de erro que o banco retornar
        except mysql.connector.Error as error:
            flash(f"Falha ao inserir dados! Erro: {error}", "Erro")

        #Após a função ser executada, encerra a conexão com o banco
        finally:
            if connection().is_connected():
                cnx.close()

    elif(table == "categorias"):
        #Abre a conexão com o banco de dados
        cnx = connection()

        #Tenta realizar operação de inserção de uma nova categoria
        try:
            #Define uma variável para facilicar a utilização do cursor de banco de dados
            with cnx.cursor() as cursor:
                insert = f"INSERT INTO {table} (nome, id_categoria_pai) VALUES (%s, %s)"
                cursor.execute(insert, args)

                #Realiza efetivamente operação de gravar os dados na tabela
                cnx.commit()
                flash("Categoria cadastrado com sucesso!", "Sucesso")

        #Caso não consiga inserir no banco, pega e exibe mensagem de erro que o banco retornar
        except mysql.connector.Error as error:
            flash(f"Falha ao inserir dados! Erro: {error}", "Erro")

        #Após a função ser executada, encerra a conexão com o banco
        finally:
            if connection().is_connected():
                cnx.close()

#Função de delete/exclusão dos dados nas tabela escolhida
def delete(table, id):
    if table == "usuarios":
        cnx = connection()

        try:
            #Define uma variável para facilicar a utilização do cursor de banco de dados
            with cnx.cursor() as cursor:
                #Variável que guarda query de exclusão da tabela e ID escolhidos/passados
                deleteQ = f"delete from {table} where id = {id}"
                cursor.execute(deleteQ)

                #Realiza efetivamente operação de gravar os dados na tabela
                cnx.commit()
                #Retorna uma mensagem de "bem-sucessido"
                return f"Usuário ID {id} deletado!"

        #Caso não consiga deletar no banco, pega e exibe mensagem de erro que o banco retornar
        except mysql.connector.Error as error:
            return f"Falha ao excluir dados! Erro: {error}"

        #Após a função ser executada, encerra a conexão com o banco
        finally:
            if connection().is_connected():
                cnx.close()

    elif table == "produtos":
        cnx = connection()

        try:
            #Define uma variável para facilicar a utilização do cursor de banco de dados
            with cnx.cursor() as cursor:
                deleteQ = f"delete from {table} where id = {id}"
                cursor.execute(deleteQ)

                #Realiza efetivamente operação de gravar os dados na tabela
                cnx.commit()
                return f"Produto ID {id} deletado!"

        #Caso não consiga deletar no banco, pega e exibe mensagem de erro que o banco retornar
        except mysql.connector.Error as error:
            return f"Falha ao excluir dados! Erro: {error}"

        #Após a função ser executada, encerra a conexão com o banco
        finally:
            if connection().is_connected():
                cnx.close()

    elif table == "categorias":
        cnx = connection()

        try:
            #Define uma variável para facilicar a utilização do cursor de banco de dados
            with cnx.cursor() as cursor:
                updateCodPai = f"UPDATE {table} SET id_categoria_pai = NULL WHERE id = {id}"
                cursor.execute(updateCodPai)
                deleteQ = f"delete from {table} where id = {id}"
                cursor.execute(deleteQ)

                #Realiza efetivamente operação de gravar os dados na tabela
                cnx.commit()
                return f"Categoria ID {id} deletada!"

        #Caso não consiga deletar no banco, pega e exibe mensagem de erro que o banco retornar
        except mysql.connector.Error as error:
            return f"Falha ao excluir dados! Erro: {error}"

        #Após a função ser executada, encerra a conexão com o banco
        finally:
            if connection().is_connected():
                cnx.close()          

#Função de select/busca dos dados da tabela escolhida/passada a função
def select(table):
    if(table == "usuarios"):
        cnx = connection()

        try:
            with cnx.cursor() as cursor:
                #Executa busca na tabela escolhida
                cursor.execute(f"select * from {table}")
                #Busca todos os dados da tabela
                result = cursor.fetchall()

                #Retorna valores para uma variável do tipo lista
                return result

        except mysql.connector.Error as error:
            flash(f"Falha ao consultar dados! Erro: {error}", "Erro")

        #Após a função ser executada, encerra a conexão com o banco
        finally:
            if connection().is_connected():
                cnx.close()

    elif(table == "produtos"):
        cnx = connection()

        try:
            with cnx.cursor() as cursor:
                cursor.execute("select * from produtos")
                result = cursor.fetchall()
            
                return result

        except mysql.connector.Error as error:
            flash(f"Falha ao consultar dados! Erro: {error}", "Erro")

        #Após a função ser executada, encerra a conexão com o banco
        finally:
            if connection().is_connected():
                cnx.close()

    elif(table == "categorias"):
        cnx = connection()

        try:
            with cnx.cursor() as cursor:
                cursor.execute("select * from categorias")
                result = cursor.fetchall()
            
                return result

        except mysql.connector.Error as error:
            flash(f"Falha ao consultar dados! Erro: {error}", "Erro")

        #Após a função ser executada, encerra a conexão com o banco
        finally:
            if connection().is_connected():
                cnx.close()

    elif(table == "status_produtos"):
        cnx = connection()

        try:
            with cnx.cursor() as cursor:
                cursor.execute("select * from status_produtos")
                result = cursor.fetchall()
            
                return result

        except mysql.connector.Error as error:
            flash(f"Falha ao consultar dados! Erro: {error}", "Erro")

        #Após a função ser executada, encerra a conexão com o banco
        finally:
            if connection().is_connected():
                cnx.close()

#Função de update/atualização/alteração, recebe a tabela, o ID do item e os valores a serem alterados
def update(table, id, *args):   
    if table == "usuarios":
        cnx = connection()

        try:
            with cnx.cursor() as cursor:
                #Variável que guarda query de update com os valores a serem alterados
                updateQ = f"UPDATE {table} SET email = %s, nome = %s, sobrenome = %s, ativo = %s WHERE id = {id}"
                cursor.execute(updateQ, args)

                #Realiza operação de gravar os dados alterados na tabela
                cnx.commit()
                #Retorna a mensagem de operação bem sucedida
                return "Usuário alterado com sucesso!"

        except mysql.connector.Error as error:
            return f"Falha ao alterar dados! Erro: {error}"

        #Após a função ser executada, encerra a conexão com o banco
        finally:
            if connection().is_connected():
                cnx.close()

    elif table == "produtos":
        cnx = connection()

        try:
            with cnx.cursor() as cursor:
                updateQ = f"UPDATE {table} SET cod_barras = %s, descricao = %s, id_status_produto = %s, preco_normal = %s, preco_com_desconto = %s, quantidade = %s WHERE id = {id}"
                cursor.execute(updateQ, args)

                #Realiza operação de gravar os dados alterados na tabela
                cnx.commit()
                #Retorna a mensagem de operação bem sucedida
                return "Produto alterado com sucesso!"

        except mysql.connector.Error as error:
            return f"Falha ao alterar dados! Erro: {error}"

        #Após a função ser executada, encerra a conexão com o banco
        finally:
            if connection().is_connected():
                cnx.close() 

    elif table == "categorias":
        cnx = connection()

        try:
            with cnx.cursor() as cursor:
                updateQ = f"UPDATE {table} SET nome = %s, id_categoria_pai = %sWHERE id = {id}"
                cursor.execute(updateQ, args)

                #Realiza operação de gravar os dados alterados na tabela
                cnx.commit()
                #Retorna a mensagem de operação bem sucedida
                return "Categoria alterado com sucesso!"

        except mysql.connector.Error as error:
            return f"Falha ao alterar dados! Erro: {error}"

        #Após a função ser executada, encerra a conexão com o banco
        finally:
            if connection().is_connected():
                cnx.close() 

#Função de select/busca dos dados do item a ser alteado, recebendo a tabela a qual irá alterar e ID 
def upSelect(table, id):
    if(table == "usuarios"):
        cnx = connection()

        try:
            with cnx.cursor() as cursor:
                #Executa query de busca da tabela escolhida e do item a ser alterado, trazendo todos seus dados
                cursor.execute(f"select * from {table} where id={id}")
                result = cursor.fetchall()
            
                return result

        except mysql.connector.Error as error:
            flash(f"Falha ao consultar dados! Erro: {error}", "Erro")

        #Após a função ser executada, encerra a conexão com o banco
        finally:
            if connection().is_connected():
                cnx.close()
    
    elif(table == "produtos"):
        cnx = connection()

        try:
            with cnx.cursor() as cursor:
                cursor.execute(f"select * from {table} where id={id}")
                result = cursor.fetchall()
            
                return result

        except mysql.connector.Error as error:
            flash(f"Falha ao consultar dados! Erro: {error}", "Erro")

        #Após a função ser executada, encerra a conexão com o banco
        finally:
            if connection().is_connected():
                cnx.close()

    elif(table == "categorias"):
        cnx = connection()

        try:
            with cnx.cursor() as cursor:
                cursor.execute(f"select * from {table} where id={id}")
                result = cursor.fetchall()
            
                return result

        except mysql.connector.Error as error:
            flash(f"Falha ao consultar dados! Erro: {error}", "Erro")

        #Após a função ser executada, encerra a conexão com o banco
        finally:
            if connection().is_connected():
                cnx.close()

#Função que trás listagem de produtos e suasTAGs.
def productListTag():
    cnx = connection()

    try:
        with cnx.cursor() as cursor:
           # cursor.execute(f"SELECT p.cod_barras, p.descricao AS 'Produto', t.nome AS 'Tag', p.preco_normal AS 'Preco' FROM produtos AS p LEFT JOIN produtos_tags AS pt ON p.id = pt.id_produto LEFT JOIN tags AS t ON pt.id_tag = t.id")
            #Executa query na respectiva view e trás todos os dados
            cursor.execute(f"SELECT * from view_produtos_com_tag")
            #Busca todas linhas da tabela e apresenta elas
            result = cursor.fetchall()
        
            return result

    except mysql.connector.Error as error:
        flash(f"Falha ao consultar dados! Erro: {error}", "Erro")

    #Após a função ser executada, encerra a conexão com o banco
    finally:
        if connection().is_connected():
            cnx.close()

#Função que trás a listagem de compras do usuário, onde recebe o ID do usuário a ser pesquisado.
def userBuys(id):
    cnx = connection()

    try:
        with cnx.cursor() as cursor:
            #Executa query na respectiva view e trás todos os dados
            cursor.execute(f"SELECT * from view_compras_do_usuario where id_usuario = {id}")
            #Busca todas linhas da tabela e apresenta elas
            result = cursor.fetchall()
        
            return result

    except mysql.connector.Error as error:
        flash(f"Falha ao consultar dados! Erro: {error}", "Erro")

    #Após a função ser executada, encerra a conexão com o banco
    finally:
        if connection().is_connected():
            cnx.close()

#Função que apresentara listagem de produtos por uma determinada TAG.
def productListPerTag(id):
    cnx = connection()

    try:
        with cnx.cursor() as cursor:
            #Executa query na respectiva view e trás todos os dados
            cursor.execute(f"SELECT * from view_produtos_com_tag where idTag = {id}")
            #Busca todas linhas da tabela e apresenta elas
            result = cursor.fetchall()
        
            return result

    except mysql.connector.Error as error:
        flash(f"Falha ao consultar dados! Erro: {error}", "Erro")

    #Após a função ser executada, encerra a conexão com o banco
    finally:
        if connection().is_connected():
            cnx.close() 

#Função para executar um select de uma tabela passada pela URL
def selectURL(table):
    cnx = connection()

    try:
        with cnx.cursor() as cursor:
            cursor.execute(f"SELECT * FROM {table}")
            result = cursor.fetchall()
        
            return result

    except mysql.connector.Error as error:
        return f"Falha ao consultar dados! Erro: {error}"

    #Após a função ser executada, encerra a conexão com o banco
    finally:
        if connection().is_connected():
            cnx.close() 
