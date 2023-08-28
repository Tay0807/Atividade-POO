class forma:
    def __init__(self,base=0,altura=0):
        self.base = base
        self.altura = altura

class quadradao(forma):
    def __init__(self,base,altura):
        super().__init__(base,altura)
    def area(self):
        print(f'A área do quadrado é {self.base*self.altura}')

class triangulo(forma):
    def __init__(self,base,altura):
        super().__init__(base,altura)
    def area(self):
        print(f'A área do triangulo é {(self.base*self.altura)/2}')


quadrado = quadradao(8,8)
quadrado.area()
triangul = triangulo(4,9)
triangul.area()