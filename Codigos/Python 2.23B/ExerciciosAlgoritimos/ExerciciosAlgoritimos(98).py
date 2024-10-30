import os
os.system('cls')

#Funcao que executa o calculo
def crediario(salario_bruto):
   
    #Parametro 30% do salario bruto declarado como variavel, para caso precise de alteracao
    parametro = (salario_bruto * 0.3)
    print(parametro)
   
    if salario_bruto <= parametro: 
        print('Emprestimo negado')
    
    else: print('Emprestimo concedido')
    
    return crediario

#Input dos objetos de calculo
salario_bruto = float(input('Digite o salario: '))
prestacao = float(input('Digite o valor da prestacao: '))

#Apresentacao do resultado
decisao_emprestimo = crediario(salario_bruto)

print(decisao_emprestimo)