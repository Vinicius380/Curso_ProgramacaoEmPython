import os
os.system('cls')

#Criando um dicionario vazio
meu_dicionario = {}

#Adicionando pares chave-valor
meu_dicionario["nome"] = "Huguinho"
meu_dicionario["endereco"] = "Rua logo ali"
meu_dicionario["telefone"] = 12345678
meu_dicionario["email"] = "h@uguinho.com.br"

#Acessando valores por chave
nome = meu_dicionario["nome"]
endereco = meu_dicionario["endereco"]

print(f"Nome: {nome}")
print(f"Endereço: {endereco}")

if "cep" in meu_dicionario:
    cep = meu_dicionario["cep"]
    print(f'Cep: {cep}')
else:
    print(f"Chave 'cep' não está nesse dicionario")

try:
    cep = meu_dicionario["cep"]
    print(f'Cep: {cep}')
except:
    print("Chave 'cep' não encontrado no dicionário")
    