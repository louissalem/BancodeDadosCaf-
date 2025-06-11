import sqlite3

# Conexão com o banco
conexao = sqlite3.connect("Empresa.db")
cursor = conexao.cursor()

# Criação da tabela
cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS Item (
        id_Produto INTEGER PRIMARY KEY AUTOINCREMENT,
        valor_Unit REAL NOT NULL,
        quantidade INTEGER NOT NULL
    );
    '''
)

conexao.commit()
cursor.close()
conexao.close()

print("✅ Tabela 'Item' criada com sucesso!")
