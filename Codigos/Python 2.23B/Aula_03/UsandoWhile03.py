import os
os.system('cls')

#Calculo da tabuada
numero = int(input("Digite o numero que será multiplicado: "))
cont = 0

while (cont<=10):
    resultado = numero*cont
    print(numero, "X", cont," : ", resultado)
    
    cont+=1
    
#Repositorio de comentarios:

#Incremento do contador sempre no final do laço
#O printa dentro do laço está retornando as execuções dos laços