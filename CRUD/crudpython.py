import mysql.connector 

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'debinha',
    password = '1123',
    database = 'bdteste'
)

cursor = conexao.cursor()

# CREATE 

"""nome_produto = "molho"
valor = 4
comando = f'INSERT INTO vendas (nome_produto, valor) VALUES("{nome_produto}", {valor})'
cursor.execute(comando)
conexao.commit()
"""

# READ 
"""
comando01 = 'SELECT * FROM vendas'
cursor.execute(comando01)
resultado = cursor.fetchall()
print(resultado)
"""
# DELETE 
# UPDATE 

cursor.close()
conexao.close()