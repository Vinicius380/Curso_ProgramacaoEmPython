import os
os.system('cls')

#Com If e Else
numero = int(input('Insira o numero: '))

def divisivel(numero):
    if (numero % 10 == 0):
        print('Divisivel por 10')
    elif (numero % 5 == 0):
        print('Divisivel por 5')
    elif (numero % 2 == 0):
        print('Divisivel por 2')

divisivel(numero)