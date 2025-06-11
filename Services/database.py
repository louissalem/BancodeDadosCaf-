#Sevices/database.py
import sqlite3
from pathlib import Path

class Database:
    def __init__(self):
        self.db_path = Path(__file__).parent.parent / 'db.db'
        self.conn = None
        self.cursor = None

    def connect(self):
        """Estabelece conexão com o banco de dados"""
        try:
            self.conn = sqlite3.connect(str(self.db_path))
            self.cursor = self.conn.cursor()
            return True
        except sqlite3.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return False

    def disconnect(self):
        """Fecha a conexão com o banco de dados"""
        if self.conn:
            self.conn.close()

    def create_tables(self):
        """Cria as tabelas necessárias no banco de dados"""
        try:
            self.connect()
            
            # Tabela de Funcionários
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS funcionarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    cargo TEXT NOT NULL,
                    email TEXT UNIQUE,
                    telefone TEXT
                )
            ''')

            # Tabela de Produtos
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS produtos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    preco REAL NOT NULL,
                    estoque INTEGER DEFAULT 0,
                    descricao TEXT
                )
            ''')

            # Tabela de Vendas
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS vendas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    data_venda TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    funcionario_id INTEGER,
                    total REAL NOT NULL,
                    FOREIGN KEY (funcionario_id) REFERENCES funcionarios (id)
                )
            ''')

            # Tabela de Itens de Venda
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS itens_venda (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    venda_id INTEGER,
                    produto_id INTEGER,
                    quantidade INTEGER NOT NULL,
                    preco_unitario REAL NOT NULL,
                    FOREIGN KEY (venda_id) REFERENCES vendas (id),
                    FOREIGN KEY (produto_id) REFERENCES produtos (id)
                )
            ''')

            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Erro ao criar tabelas: {e}")
            return False
        finally:
            self.disconnect()
