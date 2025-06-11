import streamlit as st
from Services.database import Database
from datetime import datetime

def show_venda_page():
    st.header("Registro de Vendas")
    
    # Inicializa o banco de dados
    db = Database()
    
    # Formulário para registrar venda
    with st.form("form_venda"):
        # Selecionar funcionário
        if db.connect():
            try:
                db.cursor.execute("SELECT id, nome FROM funcionarios")
                funcionarios = db.cursor.fetchall()
                funcionario_options = {f"{f[1]} (ID: {f[0]})": f[0] for f in funcionarios}
                funcionario_selected = st.selectbox("Funcionário", list(funcionario_options.keys()))
                funcionario_id = funcionario_options[funcionario_selected]
            except Exception as e:
                st.error(f"Erro ao carregar funcionários: {e}")
                funcionario_id = None
            finally:
                db.disconnect()
        
        # Selecionar produtos
        if db.connect():
            try:
                db.cursor.execute("SELECT id, nome, preco, estoque FROM produtos WHERE estoque > 0")
                produtos = db.cursor.fetchall()
                produto_options = {f"{p[1]} (R${p[2]:.2f} - Estoque: {p[3]})": p[0] for p in produtos}
                produto_selected = st.selectbox("Produto", list(produto_options.keys()))
                produto_id = produto_options[produto_selected]
                
                quantidade = st.number_input("Quantidade", min_value=1, max_value=produtos[produto_id-1][3])
            except Exception as e:
                st.error(f"Erro ao carregar produtos: {e}")
                produto_id = None
                quantidade = 0
            finally:
                db.disconnect()
        
        submitted = st.form_submit_button("Registrar Venda")
        
        if submitted and funcionario_id and produto_id:
            if db.connect():
                try:
                    # Inserir venda
                    db.cursor.execute("""
                        INSERT INTO vendas (funcionario_id, total)
                        VALUES (?, ?)
                    """, (funcionario_id, produtos[produto_id-1][2] * quantidade))
                    venda_id = db.cursor.lastrowid
                    
                    # Inserir item da venda
                    db.cursor.execute("""
                        INSERT INTO itens_venda (venda_id, produto_id, quantidade, preco_unitario)
                        VALUES (?, ?, ?, ?)
                    """, (venda_id, produto_id, quantidade, produtos[produto_id-1][2]))
                    
                    # Atualizar estoque
                    db.cursor.execute("""
                        UPDATE produtos 
                        SET estoque = estoque - ? 
                        WHERE id = ?
                    """, (quantidade, produto_id))
                    
                    db.conn.commit()
                    st.success("Venda registrada com sucesso!")
                except Exception as e:
                    st.error(f"Erro ao registrar venda: {e}")
                finally:
                    db.disconnect()
    
    # Exibir histórico de vendas
    if db.connect():
        try:
            db.cursor.execute("""
                SELECT v.id, f.nome, v.data_venda, v.total, p.nome, iv.quantidade
                FROM vendas v
                JOIN funcionarios f ON v.funcionario_id = f.id
                JOIN itens_venda iv ON v.id = iv.venda_id
                JOIN produtos p ON iv.produto_id = p.id
                ORDER BY v.data_venda DESC
            """)
            vendas = db.cursor.fetchall()
            
            if vendas:
                st.subheader("Histórico de Vendas")
                for venda in vendas:
                    st.write(f"Venda #{venda[0]} | Funcionário: {venda[1]} | Data: {venda[2]} | Total: R${venda[3]:.2f}")
                    st.write(f"Produto: {venda[4]} | Quantidade: {venda[5]}")
                    st.write("---")
            else:
                st.info("Nenhuma venda registrada.")
        except Exception as e:
            st.error(f"Erro ao carregar vendas: {e}")
        finally:
            db.disconnect() 