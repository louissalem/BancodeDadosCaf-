import sqlite3

# Conexão com o banco
def conectar():
    return sqlite3.connect("db.db")

# Criar a tabela 'produto'
def criar_tabela_produto():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produto (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descricao TEXT NOT NULL,
            val_unitario REAL NOT NULL,
            id_fornecedores INTEGER NOT NULL
        );
    """)

    conexao.commit()
    cursor.close()
    conexao.close()

    print("✅ Tabela 'produto' criada com sucesso!")

# Adicionar novo produto
def adicionar_produto(descricao, val_unitario, id_fornecedores):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO produto (descricao, val_unitario, id_fornecedores)
        VALUES (?, ?, ?)
    """, (descricao, val_unitario, id_fornecedores))

    conexao.commit()
    cursor.close()
    conexao.close()

    print("✅ Produto adicionado com sucesso!")

# Listar todos os produtos
def listar_produtos():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM produto")
    produtos = cursor.fetchall()

    cursor.close()
    conexao.close()

    return produtos

# Buscar produto por ID
def buscar_produto_por_id(produto_id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM produto WHERE id = ?", (produto_id,))
    produto = cursor.fetchone()

    cursor.close()
    conexao.close()

    return produto

# Atualizar produto
def atualizar_produto(produto_id, descricao, val_unitario, id_fornecedores):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE produto
        SET descricao = ?, val_unitario = ?, id_fornecedores = ?
        WHERE id = ?
    """, (descricao, val_unitario, id_fornecedores, produto_id))

    conexao.commit()
    cursor.close()
    conexao.close()

    print("✅ Produto atualizado com sucesso!")

# Deletar produto
def deletar_produto(produto_id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM produto WHERE id = ?", (produto_id,))
    conexao.commit()

    cursor.close()
    conexao.close()

    print("✅ Produto deletado com sucesso!")

# Executa a criação da tabela se for o script principal
if __name__ == "__main__":
    criar_tabela_produto()

    # Exemplos de uso:
    # adicionar_produto("Coca-Cola 2L", 8.50, 1)
    # print(listar_produtos())
    # print(buscar_produto_por_id(1))
    # atualizar_produto(1, "Coca-Cola 2L", 9.00, 2)
    # deletar_produto(1)
