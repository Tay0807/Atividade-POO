class item:
    def __init__(self,nome,preco):
        self.nome = nome
        self.preco = preco
    def calcular_valor(self):
        return 20

class Produto(item):
    def calcular_valor(self):
        print('O valor do produto é: ',super().calcular_valor()*4)


produto1 = Produto('batata',20.00)
produto1.calcular_valor()