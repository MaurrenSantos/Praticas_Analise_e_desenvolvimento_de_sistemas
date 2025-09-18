import sqlite3

# 1. Conectar ao banco de dados (ou criar um novo)
# usando a função connect do módulo sqlite3 para se conectar a um banco de dados SQLite
# Chamando "exemplo.db". Se o banco de dados não existir, ele será criado automaticamente.
conn = sqlite3.connect('exemplo.db')

# 2. Criar um objeto cursor
# O cursor é usado para executar comandos SQL no banco de dados.
# Ele atua como uma espécie de ponteiro que percorre os resultados de consultas.
cursor = conn.cursor()

# 3. Definir o comando SQL para criar a tabela
# define uma string create_table que contém um comando SQL, para criar uma tabela chamada "Produtos".
# Esta tabela terá quatro colunas: id (chave primária), nome (texto), preço (número real) e estoque (número inteiro).
create_table = """
CREATE TABLE IF NOT EXISTS Produtos (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    preco REAL NOT NULL,
    estoque INTEGER
    );
"""
# Usa o método execute do objeto cursor para executar o comando SQL, definido anteriormetne e criar a tabela no banco de dados.
# 4. Executar o comando SQL para criar a tabela
cursor.execute(create_table)

# 5. Confirmar as alterções (commit)
# Após a execução bem-sucedida do comando SQL, usa o método commit no objeto de conexão (conn) para confirmar as alterações no banco de dados
# Isso garante que as alterações sejam efetivamente aplicadas.
conn.commit()

# 6. Fechar a conexão com o banco de dados
# Finalmente você usa o método close no objeto de conexão para encerrar a conexão com o banco de dados.
# É uma prática recomendada dechar a conexão após a conclusão das operações, para liberar recursos e evitar possíveis problemas de concorrência
conn.close()
############################################################################################

#Prática

# Adicionar produto
import sqlite3
# Conectando ao banco de dados
conn = sqlite3.connect('exemplo.db')
cursor = conn.cursor()
# Dados do novo produto
novo_produto = ("Camiseta", 29.99, 50)
# Comando SQL para inserir o novo produto na tabela
inserir_produto = "INSERT INTO Produtos (nome, preco, estoque) VALUES (?, ?, ?)"
# Executando o comando SQL para inserção
cursor.execute(inserir_produto, novo_produto)
# Confirmando as alterações
conn.commit()
# Fechando a conexão
conn.close()
# Visualizar produto
# Conectando ao banco de dados
conn = sqlite3.connect("exemplo.db")
cursor = conn.cursor()
# Comando SQL para selecionar todos os produtos
selecionar_produtos = "SELECT * FROM Produtos"
# Executando o comando SQL
cursor.execute(selecionar_produtos)
# Obtendo todos os registros e exibindo-os
produtos = cursor.fetchall()
for produto in produtos:
    print(produto)
# Fechando a conexão
conn.close()

# Atualizar produto
import sqlite3
# Conectando ao banco de dados
conn = sqlite3.connect("exemplo.db")
cursor = conn.cursor()
# Novo preço e ID do produto a ser atualizado
novo_preco = 24.99
produto_id = 1 # Suponhamos que queremos atualizar o produto com ID 1
# Comando SQL par atualizar o preço do produto
atualizar_preco = "UPDATE Produtos SET preco = ? WHERE id = ?"
# Executando o comando SQL de atualização
cursor.execute(atualizar_preco, (novo_preco, produto_id))
# Confirmando as alterações
conn.commit()
# Fechando a conexão
conn.close()
# Excluir produto
import sqlite3
# Conectando ao banco de dados
conn = sqlite3.connect('exemplo.db')
cursor = conn.cursor()
# ID do produto a ser excluído
produto_id = 1
# Comando SQL para excluir o produto
excluir_produto = "DELETE FROM Produtos WHERE id = ?"
# Executando o comando SQL de exclusão
cursor.execute(excluir_produto, (produto_id,))
# Confirmando as alterações
conn.commit()
# Fechando a conexão
conn.close() 

