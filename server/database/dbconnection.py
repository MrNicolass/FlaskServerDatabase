import mysql.connector

#Define a conexão do banco de dados
cnx = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="MtMsH@+6XDZi"
)

#Define uma variável para facilicar a utilização do cursos de banco de dados
dbcursor = cnx.cursor()

def teste():
    dbcursor.execute("select * from arte.artistas")
    myresult = dbcursor.fetchall()
    for x in myresult:
        print(x)
