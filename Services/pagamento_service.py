import sqlite3

# Função para conectar ao banco
def conectar():
    return sqlite3.connect("db.db")

# Função para criar a tabela 'pagamento'
def criar_tabela_pagamento():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pagamento (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente TEXT NOT NULL,
            tipo_pagamento TEXT NOT NULL,
            dinheiro REAL DEFAULT 0,
            pix REAL DEFAULT 0,
            cartao REAL DEFAULT 0
        );
    """)

    conexao.commit()
    cursor.close()
    conexao.close()

    print("✅ Tabela 'pagamento' criada com sucesso!")

# Função para adicionar um pagamento
def adicionar_pagamento(cliente, tipo_pagamento, dinheiro=0, pix=0, cartao=0):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO pagamento (cliente, tipo_pagamento, dinheiro, pix, cartao)
        VALUES (?, ?, ?, ?, ?)
    """, (cliente, tipo_pagamento, dinheiro, pix, cartao))

    conexao.commit()
    cursor.close()
    conexao.close()

    print("✅ Pagamento registrado com sucesso!")

# Função para listar todos os pagamentos
def listar_pagamentos():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM pagamento")
    pagamentos = cursor.fetchall()

    cursor.close()
    conexao.close()

    return pagamentos

# Função para buscar pagamento por ID
def buscar_pagamento_por_id(pagamento_id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM pagamento WHERE id = ?", (pagamento_id,))
    pagamento = cursor.fetchone()

    cursor.close()
    conexao.close()

    return pagamento

# Função para atualizar um pagamento
def atualizar_pagamento(pagamento_id, cliente, tipo_pagamento, dinheiro, pix, cartao):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE pagamento
        SET cliente = ?, tipo_pagamento = ?, dinheiro = ?, pix = ?, cartao = ?
        WHERE id = ?
    """, (cliente, tipo_pagamento, dinheiro, pix, cartao, pagamento_id))

    conexao.commit()
    cursor.close()
    conexao.close()

    print("✅ Pagamento atualizado com sucesso!")

# Função para deletar um pagamento
def deletar_pagamento(pagamento_id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM pagamento WHERE id = ?", (pagamento_id,))
    conexao.commit()

    cursor.close()
    conexao.close()

    print("✅ Pagamento deletado com sucesso!")

# Criar tabela se este arquivo for executado diretamente
if __name__ == "__main__":
    criar_tabela_pagamento()

    # Exemplos de uso:
    # adicionar_pagamento("Maria", "pix", dinheiro=0, pix=150.0, cartao=0)
    # print(listar_pagamentos())
    # print(buscar_pagamento_por_id(1))
    # atualizar_pagamento(1, "Maria", "dinheiro", 100.0, 0, 0)
    # deletar_pagamento(1)
