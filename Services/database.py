#Sevices/database.py
import sqlite3

server = ''
username = ''
password = ''
database = 'db.db'
conexao = sqlite3.connect(database)
print("Banco de dados cafe coelho criado com sucesso!")
