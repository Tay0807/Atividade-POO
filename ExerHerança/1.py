class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

class Aluno(Pessoa):
    def __init__(self,nome,idade,matricula):
        super().__init__(nome,idade)
        self.matricula = matricula


aluno1 = Aluno('Tayná',16,2764)
print(aluno1.nome)
print(aluno1.idade)
print(aluno1.matricula)