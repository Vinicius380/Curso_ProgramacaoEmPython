import os
os.system('cls')

saldo = 1000

while (True):
    operacao = input("Digite a operação (saque/deposito/sair): ").lower()
    if (operacao == "sair"): 
        break
    elif (operacao == "saque"):
        valor = int(input("Digite o valor para saque: "))
        if (valor>saldo):
            print("Saldo insuficiente para saque")
        else:
            saldo = saldo-valor
            print(f"Saque realizado com sucesso! saldo atual: R${saldo}")
    elif (operacao=="deposito"):
        deposito = int(input("Digite o valor para Deposito: "))
        saldo = saldo+deposito
        print(f"Deposito realizado com sucesso! saldo atual: R${saldo}")
    else:
        print("Operação Invalida!")
        
#Repositorio de comentarios:

#01 O encademaneto do IF dentro do ELIF esta verificando apenas se o input operação for igual
#A uma das opções, é feita a verificação por opção