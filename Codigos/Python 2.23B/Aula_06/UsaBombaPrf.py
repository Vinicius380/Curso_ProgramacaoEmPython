
#Código do professor

import time

class BombaDagua:
    def __init__(self):
        self.status = False #Bomba inicialmente desligada
        self.tempo_ligada = 0 #Tempo que a bomba ficará ligada (em segundos)
    
    def ligar(self, tempo_ligada):
        if self.status: #Evita ligar a bomba se já estiver ligada
            print("A bomba já está ligada!")
            return
        
        self.status = True #Liga a bomba
        self.tempo_ligada = tempo_ligada #Define o tempo que a bomba ficará ligada
        
        while self.status: #Loop enquanto a bomba estiver ligada
            self.tempo_ligada -= 1 #Decrementa o tempo restante

            if self.tempo_ligada == 0:  #Bomba desliga após o tempo definido
                self.desligar()
                break
        
        print(f'Tempo restante: `{self.tempo_ligada} segndos')
        time.sleep(1)   #Aguarda 1 segundo antes de atualizar a mensagem
        
    def desligar(self):
        if not self.status:   #Evita desligar a bomba se ja estiver desligada
         print("A bomba já está desligada")
         
        self.status = False #Desliga a bomba
        print("Bomba desligada!")
        
#Exemplo de uso:
bomba = BombaDagua()
bomba.ligar(10)    #Liga a bomba por 10 segundos