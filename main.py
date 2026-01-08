import streamlit as st
import sqlite3

# 1 - Conexão (usando check_same_thread para evitar erros no Streamlit)
conexao = sqlite3.connect('BancoSantos.db', check_same_thread=False)
cursor = conexao.cursor()

# 2 - Criando a tabela (Adicionado IF NOT EXISTS e corrigido DEFAULT)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS banco(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL UNIQUE,
        senha TEXT NOT NULL,
        saldo REAL NOT NULL,
        tipo TEXT NOT NULL CHECK(tipo IN ('Corrente','Poupanca')),
        status TEXT NOT NULL DEFAULT 'Ativo'
    )       
""")
conexao.commit()

# --- INTERFACE DO STREAMLIT ---
st.title("Cadastro Banco Santos")

nome = st.text_input("Nome do Titular")
senha = st.text_input("Senha", type="password")

# ADICIONE ESTA LINHA ABAIXO:
senha_confirmar = st.text_input("Confirme sua Senha", type="password")

saldo = st.number_input("Saldo Inicial", min_value=0.0)
tipo = st.selectbox("Tipo de Conta", ["Corrente", "Poupanca"])

if st.button("Finalizar Cadastro"):
    # 1. Verifica se o nome já existe no banco
    cursor.execute("SELECT nome FROM banco WHERE nome = ?", (nome,))
    usuario_existente = cursor.fetchone()

    # 2. Lógica de decisão
    if nome == "":
        st.error("Por favor, preencha o nome.")
    
    elif usuario_existente:
        st.error(f"O nome '{nome}' já está cadastrado. Escolha outro nome.")
    
    # Agora esta linha vai funcionar porque a variável existe!
    elif senha != senha_confirmar:
        st.error("As senhas não coincidem.")
        
    else:
        # Se passou em tudo, faz o INSERT
        cursor.execute(
            "INSERT INTO banco (nome, senha, saldo, tipo) VALUES (?, ?, ?, ?)",
            (nome, senha, saldo, tipo)
        )
        conexao.commit()
        st.success(f"Conta de {nome} criada com sucesso!")

if st.button("Apagar todos os dados"):
    cursor.execute("DELETE FROM banco")
    conexao.commit()
    st.warning("Todos os registros foram apagados com sucesso!")