import os
os.system('cls')

def SolicitarValor_01():
    numero = int(input("Digite um numero: "))
    return numero

def SolicitarValor_02():
    numero = int(input("Digite um numero: "))
    return numero

def Calcular(a, b):
    total = a+b
    return total

valor = Calcular(SolicitarValor_01(), SolicitarValor_02())
print("total: ", valor)

#Repositorio de variaveis

#O return armazen o valor de um determinado calculo, função
#E é utilizado no calculo da variavel seguinte