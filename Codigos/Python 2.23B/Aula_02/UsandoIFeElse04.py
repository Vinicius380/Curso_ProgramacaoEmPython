import os
os.system('cls')

valor_compra = float(input('Insira o valor do item:' ))

print('''
        FORMAS DE PAGAMENTO
         PIX (1)
         CARTÃO DE CRÉDITO (2)
         CHEQUE (2)
      ''')

forma_pagamento = str(input('Escolha a forma de pagamento: '))

if (forma_pagamento == '1'):
    desconto = (valor_compra/100)*10
    valor_final = valor_compra - desconto
    print('Total a pagar: R$', valor_final)

elif (forma_pagamento == '2'):
    valor_final = valor_compra + (valor_compra*0.10)
    print('Total a pagar: R$', valor_final)

elif (forma_pagamento == '3'):
    valor_final = valor_compra + (valor_compra*0.15)
    print('Total a pagar: R$', valor_final)

else:
    print('Opção inválida')