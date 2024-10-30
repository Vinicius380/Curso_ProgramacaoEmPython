import math
import os
os.system('cls')

raio = float(input("Digite o valor do raio: "))

def area_circulo(raio):
    area = math.pi * raio ** 2
    return area

#raio = float(input("Digite o valor do raio: "))

area=area_circulo(raio)

print(f'A area do circulo é: {area}')