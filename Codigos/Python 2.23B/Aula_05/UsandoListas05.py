import os
os.system('cls')

def combinarListas(lista1, lista2, condicao):
    lista_combinada = []
    for elemento1,elemento2 in zip(lista1,lista2):
        if(condicao(elemento1,elemento2)):
            lista_combinada.append(elemento1)
        else:
            lista_combinada.append(elemento2)
    return lista_combinada
    
lista_numeros = [1,2,3,4,5,6]
lista_strings = ["a", "b", "c","d","e","f"]
    
condicao = lambda numero, string: numero % 2 == 0 and len(string)%2==1
lista_combinada = combinarListas(lista_numeros, lista_strings,condicao)
    
print("Lista combinada condicional: ",lista_combinada)