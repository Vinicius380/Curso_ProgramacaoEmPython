import os
os.system('cls')

class Pessoa:
    def __init__(self,nome,idade,genero,cor,cidade,interesses):
        self.nome = nome
        self.idade = idade
        self.genero = genero
        self.cor = cor
        self.cidade = cidade
        self.interesses = interesses

    @property  #Criação de propriedade
    def nome(self): 
        return self.nome
 
    
    @nome.setter
    def nome(self,novo_nome):
        if not novo_nome:
            raise ValueError("O campo nome não deve estar vazio")
        self.nome = novo_nome

    @property
    def idade(self):
        return self.idade

    @idade.setter
    def idade(self,nova_idade):
        if not isinstance(nova_idade,int)or nova_idade<0:
            raise ValueError("O campo não deve estar vazio")
        self.nome = nova_idade

    @property
    def genero(self):
        return self.genero

    @genero.setter
    def genero(self, novo_genero):
        if not novo_genero:
            raise ValueError("O genero deve ser informado")
        self.genero = novo_genero

    @property
    def cor(self):
        return self.cor

    @cor.setter
    def cor(self, nova_cor):
        if not nova_cor:
            raise ValueError("Informe a cor")
        self.cor = nova_cor

    @property
    def cidade(self):
        return self.cidade

    @cidade.setter
    def cidade(self, nova_cidade):
        if not nova_cidade:
            raise ValueError("Informe a cidade")
        self.cidade = nova_cidade

    @property
    def interesse(self):
        return self.interesse

    @interesse.setter
    def interesses(self, novos_interesses):
        if not novos_interesses:
            raise ValueError("Informe os interesses")
        self.interesses = novos_interesses



