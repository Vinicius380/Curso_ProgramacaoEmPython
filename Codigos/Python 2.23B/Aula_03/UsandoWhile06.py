import os
os.system('cls')

palavra_secreta = "outra"
letras_usadas = []
acertos = 0
erros = 0

while erros < len(palavra_secreta) and acertos < len(palavra_secreta):
    letra = input("Digite uma letra: ").lower()
    if (letra in letras_usadas):
        print("Letra já usada")
        continue
    letras_usadas.append(letra)
    
    if (letra in palavra_secreta):
        acertos += 1
        print(f"Acertou! A letra '{letra}' está na palavra")
    else:
        erros+=1
        print(f"Errou! A letra '{letra}' não está na palvra")
if (acertos == len(palavra_secreta)):
    print("Parabéns você venceu")
else:
    print(f"Você perdeu! A palvra secreta era {palavra_secreta}")