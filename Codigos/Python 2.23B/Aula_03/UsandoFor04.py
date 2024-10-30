import os
os.system('cls')

numeros = [1,2,3,4,5,6]

soma = 0
for numero in numeros:
    soma+=numero

media = soma/len(numeros)

print("A media dos numeros é: ", media)