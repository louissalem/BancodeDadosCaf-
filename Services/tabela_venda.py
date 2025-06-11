import sqlite3

# Conexão com o banco
def conectar():
    return sqlite3.connect("db.db")

# Criar a tabela 'venda'
def criar_tabela_venda():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS venda (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_cliente INTEGER NOT NULL,
            data_venda TEXT NOT NULL,
            valor_total REAL NOT NULL,
            id_forma_pagamento INTEGER NOT NULL
        );
    """)

    conexao.commit()
    cursor.close()
    conexao.close()

    print("✅ Tabela 'venda' criada com sucesso!")

# Adicionar uma nova venda
def adicionar_venda(id_cliente, data_venda, valor_total, id_forma_pagamento):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO venda (id_cliente, data_venda, valor_total, id_forma_pagamento)
        VALUES (?, ?, ?, ?)
    """, (id_cliente, data_venda, valor_total, id_forma_pagamento))

    conexao.commit()
    cursor.close()
    conexao.close()

    print("✅ Venda registrada com sucesso!")

# Listar todas as vendas
def listar_vendas():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM venda")
    vendas = cursor.fetchall()

    cursor.close()
    conexao.close()

    return vendas

# Buscar venda por ID
def buscar_venda_por_id(venda_id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM venda WHERE id = ?", (venda_id,))
    venda = cursor.fetchone()

    cursor.close()
    conexao.close()

    return venda

# Atualizar uma venda
def atualizar_venda(venda_id, id_cliente, data_venda, valor_total, id_forma_pagamento):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE venda
        SET id_cliente = ?, data_venda = ?, valor_total = ?, id_forma_pagamento = ?
        WHERE id = ?
    """, (id_cliente, data_venda, valor_total, id_forma_pagamento, venda_id))

    conexao.commit()
    cursor.close()
    conexao.close()

    print("✅ Venda atualizada com sucesso!")

# Deletar uma venda
def deletar_venda(venda_id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM venda WHERE id = ?", (venda_id,))
    conexao.commit()

    cursor.close()
    conexao.close()

    print("✅ Venda deletada com sucesso!")

# Executar a criação da tabela se rodar diretamente
if __name__ == "__main__":
    criar_tabela_venda()

    # Exemplos de uso:
    # adicionar_venda(1, "2025-05-28 15:00", 300.0, 2)
    # print(listar_vendas())
    # print(buscar_venda_por_id(1))
    # atualizar_venda(1, 1, "2025-05-28 16:00", 350.0, 3)
    # deletar_venda(1)
