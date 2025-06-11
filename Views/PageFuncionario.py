import streamlit as st
from Services.database import Database

def show_funcionario_page():
    st.header("Cadastro de Funcionários")
    
    # Inicializa o banco de dados
    db = Database()
    
    # Formulário para adicionar funcionário
    with st.form("form_funcionario"):
        nome = st.text_input("Nome do Funcionário")
        cargo = st.text_input("Cargo")
        email = st.text_input("Email")
        telefone = st.text_input("Telefone")
        
        submitted = st.form_submit_button("Cadastrar")
        
        if submitted:
            if db.connect():
                try:
                    db.cursor.execute("""
                        INSERT INTO funcionarios (nome, cargo, email, telefone)
                        VALUES (?, ?, ?, ?)
                    """, (nome, cargo, email, telefone))
                    db.conn.commit()
                    st.success("Funcionário cadastrado com sucesso!")
                except Exception as e:
                    st.error(f"Erro ao cadastrar funcionário: {e}")
                finally:
                    db.disconnect()
    
    # Exibir lista de funcionários
    if db.connect():
        try:
            db.cursor.execute("SELECT * FROM funcionarios")
            funcionarios = db.cursor.fetchall()
            
            if funcionarios:
                st.subheader("Funcionários Cadastrados")
                for func in funcionarios:
                    st.write(f"ID: {func[0]} | Nome: {func[1]} | Cargo: {func[2]} | Email: {func[3]} | Telefone: {func[4]}")
            else:
                st.info("Nenhum funcionário cadastrado.")
        except Exception as e:
            st.error(f"Erro ao carregar funcionários: {e}")
        finally:
            db.disconnect() 