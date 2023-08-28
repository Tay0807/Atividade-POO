class cachorro:
    def __init__(self, nome,idade):
        self.nome = nome
        self.idade = idade
    def latir(self):
        print("Woolf!")

auau = cachorro('totó',5)
auau.latir()