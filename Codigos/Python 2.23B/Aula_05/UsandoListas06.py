import os
os.system('cls')

def criar_estrutura_aninhada(lista_principal, lista_aninhada):
    estrutura_aninhada = []
    for elemento_principal in lista_principal:
        sublista = [elemento_principal]
        for elemento_aninhado in lista_aninhada:
            sublista.append(elemento_aninhado)
        estrutura_aninhada.append(sublista)
    return estrutura_aninhada

nomes = ["Huguinho", "Zezinho", "Luizinho"]
idade = [25, 30, 22]
estrutura_aninhada = criar_estrutura_aninhada(nomes,idade)
print("Estrutura de dados aninhada: ", estrutura_aninhada)