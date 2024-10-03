import mysql
import mysql.connector

conn = mysql.connector.connect(
    username = 'nicole',
    hostname = 'localhost',
    password = 'projeto123',
    db = 'projeto_crud'
)
if conn.is_connected():
    print("Conectado com Mysql database")
else:
    print("Falha ao conectar com Mysql database")