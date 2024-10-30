import os
os.system('cls')

nome = input('Insira o nome: ')
idade = int(input('Insira a idade: '))

print(f'''
M = Masculino
F = Feminino
      ''')

sexo = input('Insira o sexo: ').upper()

#Estrutura de decisao
if sexo == 'F' and idade < 25:
    print(f'{nome} ''\n'' Aceita')
else:
    print('Nao aceita')
