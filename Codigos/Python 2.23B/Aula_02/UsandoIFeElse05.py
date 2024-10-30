import os
os.system('cls')

altura = float(input('Insira a altura: '))
peso = float(input('Insira o peso: '))

imc = peso/(altura*altura)

if (imc < 18):
    print(f'''
Desnutrido
IMC: {imc:.2f}
     ''')

elif(18.5 < imc < 25):
    print(f'''
Ideal
IMC: {imc:.2f}
     ''')

elif (25 < imc < 30):
    print(f'''
Obeso
IMC: {imc:.2f}
     ''')

elif (imc > 30):
    print(f'''
Sobrepeso
IMC: {imc:.2f}
        ''')