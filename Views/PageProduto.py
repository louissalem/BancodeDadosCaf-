import streamlit as st
from Services.database import Database

def show_produto_page():
    st.header("Cadastro de Produtos")
    
    # Inicializa o banco de dados
    db = Database()
    
    # Formulário para adicionar produto
    with st.form("form_produto"):
        nome = st.text_input("Nome do Produto")
        preco = st.number_input("Preço", min_value=0.0, step=0.01)
        estoque = st.number_input("Estoque", min_value=0, step=1)
        descricao = st.text_area("Descrição")
        
        submitted = st.form_submit_button("Cadastrar")
        
        if submitted:
            if db.connect():
                try:
                    db.cursor.execute("""
                        INSERT INTO produtos (nome, preco, estoque, descricao)
                        VALUES (?, ?, ?, ?)
                    """, (nome, preco, estoque, descricao))
                    db.conn.commit()
                    st.success("Produto cadastrado com sucesso!")
                except Exception as e:
                    st.error(f"Erro ao cadastrar produto: {e}")
                finally:
                    db.disconnect()
    
    # Exibir lista de produtos
    if db.connect():
        try:
            db.cursor.execute("SELECT * FROM produtos")
            produtos = db.cursor.fetchall()
            
            if produtos:
                st.subheader("Produtos Cadastrados")
                for prod in produtos:
                    st.write(f"ID: {prod[0]} | Nome: {prod[1]} | Preço: R${prod[2]:.2f} | Estoque: {prod[3]} | Descrição: {prod[4]}")
            else:
                st.info("Nenhum produto cadastrado.")
        except Exception as e:
            st.error(f"Erro ao carregar produtos: {e}")
        finally:
            db.disconnect() 