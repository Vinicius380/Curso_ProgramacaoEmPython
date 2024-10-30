import os
os.system('cls')

lista = [1,2,3,4,5,6,7,8,9,10]

pares = lista[1::2]
impares = lista[0::2]

print(pares)
print(impares)

tres_ultimos = lista[-3:]
print("Os tres ultimos numeros: ", tres_ultimos)

primeiros_e_ultimos = lista[:2] + lista[-2:]
print("Primeiros e ultimos: ", primeiros_e_ultimos)