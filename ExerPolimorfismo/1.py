class Animal_aquatico:
    def nadando(self):
        pass

class Peixe(Animal_aquatico):
    def nadando(self):
        print('Olá sou o nemo')

class Tartaruga(Animal_aquatico):
    def nadando(self):
        print('Olá eu sou a tartaruga do filme procurando nemo')


peixe = Peixe()
tartaruga = Tartaruga()

peixe.nadando()
tartaruga.nadando()
