import os
os.system('cls')

#numb1 = float(input('Insira o primeiro numero: '))
#numb2 = float(input('Insira o segundo numero: '))
#numb3 = float(input('Insira o terceiro numero: '))

numeros = float(input('Insira o numero: '))
for numeros in range(0, 4):
    lista = [numeros]


maior = max(lista)
menor = min(lista)

lista.sort()
intermediario = lista[1]

print(f'''
Maior numero: {maior}
Intermediario: {intermediario}
Menor numero: {menor}
''')





