import os
os.system('cls')

lista1 = [1,2,3]
lista2 = [4,5,6]

lista_intercalada = []
i=0
j=0

while i < len(lista1) and j < len(lista2):
    lista_intercalada.append(lista1[i])
    lista_intercalada.append(lista2[j])
    i+=1 #i=i+1
    j+=1 #j=j+1

print("Lista intercalada: ", lista_intercalada)

lista_intercalada.sort()    

print("Lista organizada: ", lista_intercalada)
    