🏦 Projeto Banco Santos - Sistema de Cadastro com Streamlit & SQLite
Este projeto foi desenvolvido como parte de uma atividade de aprendizado para integrar uma interface web moderna (Streamlit) com um banco de dados relacional (SQLite). O objetivo é simular o sistema de cadastro de um banco, garantindo a integridade dos dados e a segurança básica do usuário.

🚀 Funcionalidades
Interface Intuitiva: Criação de formulários amigáveis com Streamlit.

Banco de Dados Persistente: Armazenamento de informações em arquivo .db local via SQLite3.

Validações de Segurança:

Comparação de senhas (confirmação).

Bloqueio de nomes de usuários duplicados (Unique constraint).

Restrição de tipos de conta (Check constraint).

Gestão de Dados: Comando para limpeza e reset de registros.

🧠 O que eu aprendi
Neste projeto, apliquei conceitos fundamentais de desenvolvimento:

Manipulação de SQL: Aprendi a criar tabelas com restrições (NOT NULL, UNIQUE, CHECK, DEFAULT) e a realizar operações de INSERT, SELECT e DELETE.

Integração Python + SQL: Entendi o funcionamento do cursor, a importância do commit() para salvar alterações e como evitar ataques de SQL Injection usando substituição de variáveis com ?.

Lógica de Fluxo no Streamlit: Compreendi como o Streamlit recarrega o script e como usar estados (if button) para controlar quando os dados devem ser enviados ao banco.

Tratamento de Erros: Implementação de mensagens de erro (st.error) e avisos de sucesso para melhorar a experiência do usuário (UX).

🛠️ Tecnologias Utilizadas
Python 3

Streamlit (Interface Web)

SQLite3 (Banco de Dados)

📂 Como executar o projeto
Instale o Streamlit: pip install streamlit

Clone o repositório.

Execute o comando: streamlit run seu_arquivo.py
