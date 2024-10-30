import os
os.system('cls')

print(f''' {'-'*10} Siglas {'-'*10}

Rio de Janeiro - RJ
São Paulo - SP
Minas Gerais - MG
Outros - OR
''')

estado = input('Insira a sigla do estado: ').upper()

if estado == 'RJ':
    print('Carioca')
    
elif estado == 'SP':
    print('Paulista')
    
elif estado == 'MG':
    print('Mineiro')
    
elif estado == 'OR':
    print('Outros estados')
    
