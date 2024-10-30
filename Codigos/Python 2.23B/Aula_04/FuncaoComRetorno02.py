import os
os.system('cls')

temperatura = int(input('Digite a temperatura: '))

def celsius_fahrenheit(celsius):
    fahrenheit = (celsius*9/5)+32
    return fahrenheit

celsius = celsius_fahrenheit(temperatura)
print(f'A temperatura em Fahrenheit é: {celsius}')