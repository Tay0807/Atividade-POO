class retangulo:
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura
    def calcular_area(self):
        calculo = self.base*self.altura
        print('A área do retangulo é:',calculo)


forma = retangulo(5,6)
forma.calcular_area()
