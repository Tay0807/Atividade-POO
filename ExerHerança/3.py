class produtos:
    def __init__(self,nome,preco):
        self.nome = nome
        self.preco = preco

class livro(produtos):
    def __init__(self,nome,preco,autor):
        super().__init__(nome,preco)
        self.autor = autor


class eletronico(produtos):
    def __init__(self,nome,preco,voltagem):
        super().__init__(nome,preco)
        self.voltagem = voltagem


livros = livro('É assim que acaba',49.80,'Collen')
print(livros.nome,livros.autor,livros.preco)
eletronicos = eletronico('Ventilador',280.99,220)
print(eletronicos.nome,eletronicos.preco,eletronicos.voltagem)
