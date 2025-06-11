# Services/cliente_service.py
import sqlite3
conexao = sqlite3.connect("db.db")
cursor = conexao.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS cliente (
        id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        telefone TEXT,
        cpf TEXT UNIQUE
    );
''')

conexao.commit()
cursor.close()
conexao.close()

print("✅ Tabela 'cliente' criada com sucesso!")

# ---------------------------
# VERIFICAR SE O CPF JÁ EXISTE
# ---------------------------
def validar_cpf_duplicado(cpf):
    conexao = sqlite3.connect("db.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT COUNT(*) FROM cliente WHERE cpf = ?", (cpf,))
    resultado = cursor.fetchone()[0]

    cursor.close()
    conexao.close()

    return resultado > 0  # True se já existe, False se não existe


# ---------------------------
# ATUALIZAR DADOS DE CONTATO DO CLIENTE
# ---------------------------
def atualizar_dados_cliente(id_cliente, novo_telefone, novo_nome):
    conexao = sqlite3.connect("Empresa.db")
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE cliente
        SET telefone = ?, nome = ?
        WHERE id_cliente = ?
    """, (novo_telefone, novo_nome, id_cliente))

    conexao.commit()
    cursor.close()
    conexao.close()


# ---------------------------
# BUSCAR TODOS OS PEDIDOS DE UM CLIENTE
# ---------------------------
def buscar_pedidos_do_cliente(id_cliente):
    conexao = sqlite3.connect("Empresa.db")
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT * FROM pedido WHERE cliente_id = ?
    """, (id_cliente,))
    pedidos = cursor.fetchall()

    cursor.close()
    conexao.close()
    return pedidos


# ---------------------------
# INSERIR CLIENTE (opcional para testes)
# ---------------------------
def inserir_cliente(nome, telefone, cpf):
    conexao = sqlite3.connect("Empresa.db")
    cursor = conexao.cursor()

    try:
        cursor.execute("""
            INSERT INTO cliente (nome, telefone, cpf)
            VALUES (?, ?, ?)
        """, (nome, telefone, cpf))
        conexao.commit()
        print("Cliente cadastrado com sucesso!")
    except sqlite3.IntegrityError:
        print("Erro: CPF já cadastrado!")

    cursor.close()
    conexao.close()


# ---------------------------
# TESTES
# ---------------------------
if __name__ == "__main__":
    # Teste de inserção
    inserir_cliente("Carlos Silva", "11988887777", "111.222.333-44")

    # Teste de CPF duplicado
    print(validar_cpf_duplicado("111.222.333-44"))

    # Teste de atualização
    atualizar_dados_cliente(1, "11999999999", "Carlos S. Atualizado")

    # Teste de busca de pedidos do cliente
    print(buscar_pedidos_do_cliente(1))

