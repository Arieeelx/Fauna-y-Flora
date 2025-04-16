import mysql.connector as mysql

def conectar_db():
    return mysql.connect(
        user="root",
        password="zzzzzzzzzzzz",
        host="localhost",
        database="semana8",
    )