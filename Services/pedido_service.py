import sqlite3

# Conexão com o banco de dados
def conectar():
    return sqlite3.connect("db.db")

# Criar tabela 'pedido'
def criar_tabela_pedido():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pedido (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_Item INTEGER NOT NULL,
            val_Total REAL NOT NULL,
            DataHora_Pedido TEXT NOT NULL,
            id_FormaPagamento INTEGER NOT NULL,
            mesa TEXT
        );
    """)

    conexao.commit()
    cursor.close()
    conexao.close()

    print("✅ Tabela 'pedido' criada com sucesso!")

# Adicionar um novo pedido
def adicionar_pedido(id_item, val_total, datahora_pedido, id_forma_pagamento, mesa=None):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO pedido (id_Item, val_Total, DataHora_Pedido, id_FormaPagamento, mesa)
        VALUES (?, ?, ?, ?, ?)
    """, (id_item, val_total, datahora_pedido, id_forma_pagamento, mesa))

    conexao.commit()
    cursor.close()
    conexao.close()

    print("✅ Pedido adicionado com sucesso!")

# Listar todos os pedidos
def listar_pedidos():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM pedido")
    pedidos = cursor.fetchall()

    cursor.close()
    conexao.close()

    return pedidos

# Buscar pedido por ID
def buscar_pedido_por_id(pedido_id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM pedido WHERE id = ?", (pedido_id,))
    pedido = cursor.fetchone()

    cursor.close()
    conexao.close()

    return pedido

# Atualizar um pedido
def atualizar_pedido(pedido_id, id_item, val_total, datahora_pedido, id_forma_pagamento, mesa):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE pedido
        SET id_Item = ?, val_Total = ?, DataHora_Pedido = ?, id_FormaPagamento = ?, mesa = ?
        WHERE id = ?
    """, (id_item, val_total, datahora_pedido, id_forma_pagamento, mesa, pedido_id))

    conexao.commit()
    cursor.close()
    conexao.close()

    print("✅ Pedido atualizado com sucesso!")

# Deletar um pedido
def deletar_pedido(pedido_id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM pedido WHERE id = ?", (pedido_id,))
    conexao.commit()

    cursor.close()
    conexao.close()

    print("✅ Pedido deletado com sucesso!")

# Executa a criação da tabela se for o arquivo principal
if __name__ == "__main__":
    criar_tabela_pedido()

    # Exemplos de uso:
    # adicionar_pedido(1, 150.75, "2025-05-28 14:30:00", 2, "Mesa 5")
    # print(listar_pedidos())
    # print(buscar_pedido_por_id(1))
    # atualizar_pedido(1, 1, 200.00, "2025-05-28 15:00:00", 1, "Mesa 8")
    # deletar_pedido(1)

