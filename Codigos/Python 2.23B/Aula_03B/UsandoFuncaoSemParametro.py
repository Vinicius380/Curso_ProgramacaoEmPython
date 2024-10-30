import os
os.system('cls')

def verificarPar():
    numero = int(input("Digite um valor: "))
    if(numero%2==0):
        print("Esse numero é par")
    else:
        print("Esse numero não é par")
    
verificarPar()