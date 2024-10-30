import os
os.system('cls')

def jogo_da_forca(palavra):
    letras_usadas = set()
    acertos = 0
    erros = 0
    
    palavra_com_acertos = ["-" for i in range(len(palavra))]
    while(erros < 6 and acertos < len(palavra)):
        print(" ".join(palavra_com_acertos))
        print(f"Letras Usadas: {letras_usadas}")
        letra = input("Digite uma letra: ")
        if (letra in letras_usadas):
            print("Essa letra já foi usada")
            continue
        letras_usadas.add(letra)
        if (letra in palavra):
            acertos+=1
            for i in range(len(palavra)):
                if (palavra[i]==letra):
                    palavra_com_acertos[i]=letra
        else:
            erros+=1
    if(erros == 6):
        print("Você Perdeu")
        return
    
palavra = input("Digite uma palavra: ")
jogo_da_forca(palavra)