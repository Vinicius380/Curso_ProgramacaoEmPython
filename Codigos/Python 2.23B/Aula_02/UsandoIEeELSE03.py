
import os
os.system('cls')

deposito = float(input('Digite o valor do deposito: '))
valor_saque = float(input('Digite o valor do saque: '))
saldo_conta = deposito

if (saldo_conta >= valor_saque):
    saldo_conta = saldo_conta - valor_saque
    print('Saldo disponivel em conta: ', saldo_conta)
else:
    print('Saldo Insuficiente')






""" 
def saldo_saque(saldo_conta, saldo_saque):
    saldo_saque = saldo_conta - saldo_saque

if (saldo_conta >= valor_saque):
    saldo_saque(saldo_conta, saldo_saque)
    print('Saldo disponivel: R$', saldo_saque) """