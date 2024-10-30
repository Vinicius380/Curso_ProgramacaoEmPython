import os
os.system('cls')

agenda = {
    "Docinho":["1234-5678","doci@nho.com"],
    "Florzinha":["9876-5432", "flor@zinha.com"]
}

#Acessando e imprimindo informações
nome = input("Informe o nome: ").upper()

if nome in agenda:
    numero,email = agenda[nome]
    print(f'{nome}')
    print(f'Telefone: {numero}')
    print(f'E-mail: {email}')
else:
    print(f"Contato {nome} não está na agenda")