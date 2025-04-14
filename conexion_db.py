import mysql.connector as mysql

def conectar_db():
    return mysql.connect(
        user="root",
        password="ssssssssss",
        host="localhost",
        database="semana8",
    )