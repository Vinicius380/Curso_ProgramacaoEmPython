import os
os.system('cls')
import random

def advinhar():
    numero_secreto = random.randint(1, 10)
    palpite = 0

    while (palpite != numero_secreto):
     palpite = int(input("Digite um numero "))
     if (palpite < numero_secreto):
        print("O numero secreto é maior!")
     elif (palpite>numero_secreto):
          print("Numero secreto é menor")
    print("Parabens você acertou")

advinhar()