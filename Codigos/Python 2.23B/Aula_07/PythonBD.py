import mysql.connector

#Criação do banco de dados
host = "localhost" #//192.168.0.23/ 
usuario = "root"
senha = "senai@126"
bd = "agenda"

#Conexao com o banco de dados
try:
    conexao = mysql.connector.connect(
        host = host,
        user = usuario,
        password = senha,
        database = bd 
    )
    print("Conexao realizada com sucesso!")
except mysql.connector.Error as erro:
    print(f"Falha na conexão veja erro: {erro}")
    
#Inserindo os dados na tabela do banco

def inserir(nome,endereco,telefone,email):
    if conexao is None:
        return False
     
    cursor = conexao.cursor()
    
    consulta = """INSERT INTO contato(nome, endereco,telefone,email)
                    values(%s,%s,%s,%s)"""
    valores = (nome,endereco,telefone,email)
    
    try:
        cursor.execute(consulta,valores )
        conexao.commit()
        return True
    
    except mysql.connector.Error as erro:
        print(f"Falha no cadastro dos dados veja erro: {erro}")
        conexao.rollback()
        return False

#Inserção de informações no banco de dados
contato_01 = inserir("Nome1", "Rua1", "Numero1", "Email1")
contato_02 = inserir("Nome2", "Rua2", "Numero2", "Email2")

#Verificação de erros

if contato_01:
    print("Contato 1 inserido com sucesso")
else:
    print("Erro ao inserir o contato 1")
    
if contato_02:
    print("Contato 2 inserido com sucesso")
else:
    print("Erro ao inserir o contato 2")

'''
#Funcao atualizar contato
def atualizar(nome, endereco, telefone, email, id):
    if conexao is None:
        return False
    
    cursor = conexao.cursor()

    consulta = """UPDATE contato SET nome =%s, endereco=%s, telefone=%s, email=%s, WHERE id =%s"""
    valores = (nome, endereco, telefone, email, id)
    try:
        cursor.execute(consulta, valores)
        conexao.commit()
        return True
    except mysql.connector.Error as erro:
        print(f"Falha ao atualizar o contato")
    
    finally:
        cursor.close()
        #conexao.close()

nome = "nome3"
endereco = "endereco2"
telefone = "234232"
email = "as@asd.com"
id = 1

contatoAtualizado = atualizar(nome,endereco,telefone,email,id)

if contatoAtualizado:
    print(f"Contato atualizado com sucesso")
else:
    print("Falha na atualizacao do contato")
'''

#Funcao deletar contato
def deletar(id):
    if conexao is None:
        return False

    cursor = conexao.cursor()
    
    consulta = """DELETE from contato WHERE id=%s"""
    
    valor = (id,)
    
    try:
        cursor.execute(consulta, valor)
        conexao.commit()
        return True
    
    except mysql.connector.Error as erro:
        print(f"Falha ao deletar o contato: {erro}")
        conexao.rollback()
        return False
        
contatoDeletado = deletar(46)