import mysql.connector 

# CONNECTION 
conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'debinha',
    password = '1123',
    database = 'bdteste'
)

cursor = conexao.cursor()

# CREATE 
def createValue(): 
    nome_produto = input("Digite o nome do produto: \n" )
    valor = input("Digite o valor do produto: \n")
    comando = f'INSERT INTO vendas (nome_produto, valor) VALUES("{nome_produto}", {valor})'
    cursor.execute(comando)
    conexao.commit()

# READ 
def readTable(): 
    comando01 = 'SELECT * FROM vendas'
    cursor.execute(comando01)
    resultado = cursor.fetchall() 
    print(resultado)

# DELETE 
def deleteValue(): 
    comando02 = 'DELETE FROM vendas ORDER BY idVendas DESC LIMIT 1'
    cursor.execute(comando02)
    conexao.commit()

# UPDATE  
def updateValue(): 
    nome_produto = input("Digite o Produto: \n")
    valor = input("Digite o novo valor do produto: \n")
    comando03 = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
    cursor.execute(comando03)
    conexao.commit()

opcao = input("Digite : \n 1 - para CREATE \n 2 - para READ \n 3 - para DELETE \n 4 - para UPDATE \n")

if(opcao == '1'): 
    createValue()
elif(opcao == '2'): 
    readTable()
elif(opcao == '3'): 
    deleteValue()
elif(opcao == '4'): 
    updateValue()
else: 
    print("isso não é uma opção")




cursor.close()
conexao.close()