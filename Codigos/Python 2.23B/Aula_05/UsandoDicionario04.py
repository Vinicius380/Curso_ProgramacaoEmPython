import os
os.system('cls')

estoque={
    "frutas":{
    "Maça":5,
    "Laranja":10,
    "Banana":20   
},
"legumes":{
    "Batata":30,
    "Berinjela":15,
    "Cebola":8
}}

#Acessando e imprimindo informações
secao = input("Informe a seção (Frutas/Legumes): ").lower()
produto = input("Informe o produto: ").capitalize()

if secao in estoque and produto in estoque [secao]:
    quantidade = estoque[secao][produto]
    print(f'{quantidade}X {produto} na seção {secao}')
else:
    print(f'Produto {produto} não encontrado na seção {secao}')