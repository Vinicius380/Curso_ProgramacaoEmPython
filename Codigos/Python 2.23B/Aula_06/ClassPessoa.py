import os
os.system ('cls')

class Pessoa:
    def __init__(self, nome, idade, genero, cor):
        self.nome = nome
        self.idade = idade
        self.genero = genero
        self.cor = cor

    def apresentar(self):
        print(f"Olá meu nome é:{self.nome}! Tenho {self.idade} anos,  minha cor é {self.cor} ")

    def mudarCidade(self, novaCidade):
        self.cidade = novaCidade

menino = Pessoa("Ricardo", 9, "Masculino", "moreno")
menino.nome = "Luizinho"
menino.idade =25
menino.mudarCidade("São Paulo")

menino.apresentar()
print(menino.cidade)
