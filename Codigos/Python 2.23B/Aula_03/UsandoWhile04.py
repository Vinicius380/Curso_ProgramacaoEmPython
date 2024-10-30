import os
os.system('cls')
import random

numero_secreto = random.randint(1, 10)
palpite = 0

while (palpite != numero_secreto):
    palpite = int(input("Digite um numero "))
    if (palpite < numero_secreto):
        print("O numero secreto é maior!")
    elif (palpite>numero_secreto):
        print("Numero secreto é menor")
print("Parabens você acertou")



#Repositorio de comentarios:

#O programa executa um jogo em que é necessário descobrir um numero secreto 
#que já está fixado na variavel "numero_secreto"