import os
os.system('cls')

nascimento = int(input('Insira o ano de nascimento: '))
ano_atual = int(input('Insira o ano atual: ')) 

while nascimento > ano_atual: 
    print('Data invalida')
    nascimento = int(input('Insira o ano de nascimento: '))

idade = ano_atual - nascimento

print(f'{idade} anos')