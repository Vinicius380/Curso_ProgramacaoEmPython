import os
os.system('cls')

import time

class Bomba:
    def __init__(self):
        self.status = False
        
    def ligar(self):
        self.status = True
        self.tempo = 10
        print(f'Bomb has planted')
        
        while self.status:
            self.tempo -=1
            time.sleep(1)
            print(f"Tempo para bomba detonar {self.tempo}")
            
            if self.tempo == 0:
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!Bomb as be detonated!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                break
        
    def desligar(self):
        self.status = False
        print(f'Bomba has be defuse')

UsaBomba = Bomba()