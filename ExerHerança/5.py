class empregado:
    def __init__(self,nome,salario):
        self.nome = nome
        self.salario = salario

class gerente(empregado):
    def __init__(self,nome,salario,setor):
        super().__init__(nome,salario)
        self.setor = setor


funcionario = gerente('Tayná',480,'jovem aprendiz')

print(funcionario.setor,funcionario.nome,funcionario.salario)