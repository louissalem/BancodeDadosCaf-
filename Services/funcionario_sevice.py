# Services/funcionario_service.py
import sqlite3

conexao = sqlite3.connect("db.db")
cursor = conexao.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS funcionario (
        id_funcionario INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        salario REAL,
        telefone VARCHAR,
        cpf TEXT UNIQUE
    );
''')
conexao.commit()
cursor.close()
conexao.close()

print("✅ Tabela 'funcionario' criada com sucesso!")
# ---------------------------
# BUSCAR FUNCIONÁRIO POR CPF
# ---------------------------
def buscar_funcionario_por_cpf(cpf):
    conexao = sqlite3.connect("db.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM funcionario WHERE cpf = ?", (cpf,))
    resultado = cursor.fetchone()

    cursor.close()
    conexao.close()
    return resultado  # Retorna uma tupla ou None


# ------------------------------------------
# CALCULAR SALÁRIO BASE DE UM FUNCIONÁRIO
# ------------------------------------------
def calcular_salario_base(funcionario_id):
    conexao = sqlite3.connect("Empresa.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT salario FROM funcionario WHERE id_funcionario = ?", (funcionario_id,))
    resultado = cursor.fetchone()

    cursor.close()
    conexao.close()
    if resultado:
        return resultado[0]  # valor do salário
    return None


# -------------------------------------
# LISTAR TODOS OS FUNCIONÁRIOS
# -------------------------------------
def listar_todos_funcionarios():
    conexao = sqlite3.connect("Empresa.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM funcionario")
    funcionarios = cursor.fetchall()

    cursor.close()
    conexao.close()
    return funcionarios


# -------------------------------------
# INSERIR FUNCIONÁRIO (opcional p/ testes)
# -------------------------------------
def inserir_funcionario(nome, salario, telefone, cpf):
    conexao = sqlite3.connect("Empresa.db")
    cursor = conexao.cursor()

    try:
        cursor.execute("""
            INSERT INTO funcionario (nome, salario, telefone, cpf)
            VALUES (?, ?, ?, ?)
        """, (nome, salario, telefone, cpf))
        conexao.commit()
        print("Funcionário cadastrado com sucesso!")
    except sqlite3.IntegrityError:
        print("Erro: CPF já cadastrado!")
    
    cursor.close()
    conexao.close()


# -------------------------
# TESTE DAS FUNÇÕES
# -------------------------
if __name__ == "__main__":
    # Teste de inserção
    inserir_funcionario("Ana Souza", 2500.0, "11999998888", "123.456.789-00")

    # Teste de busca por CPF
    print(buscar_funcionario_por_cpf("123.456.789-00"))

    # Teste de cálculo de salário
    print(calcular_salario_base(1))  # ou use o id correto

    # Teste de listagem de todos os funcionários
    print(listar_todos_funcionarios())
