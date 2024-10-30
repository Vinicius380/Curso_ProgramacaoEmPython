import os
os.system('cls')

#Criando um dicionário
meu_dicionario = {"Nome":"Zezinho", "idade":16, "Cidade": "Patópolis"}

#Print valor antigo
cidade_antiga = meu_dicionario["Cidade"]
print("Cidade antiga:",cidade_antiga)

#Modificando o valor de uma chave existente
meu_dicionario["Cidade"] = "ItaquaCity"

#Print valor novo
cidade_nova = meu_dicionario["Cidade"]
print("Cidade nova:",cidade_nova)

print("="*90)

#Print das chaves e valores por meio do "For"
for chave,valor in meu_dicionario.items():
    print(f'{chave}:{valor}')