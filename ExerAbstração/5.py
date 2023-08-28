class aluno:
    def __init__(self,nome,nota_um,nota_dois):
        self.nome = nome
        self.nota_um = nota_um
        self.nota_dois = nota_dois
    def media(self):
        media = (self.nota_um + self.nota_dois)/2
        print('Sua média escolar é:',media)

tayna = aluno('Tay',9,8)
tayna.media()