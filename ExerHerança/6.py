class bebidas:
    def __init__(self,nome,tipo):
        self.nome = nome
        self.tipo = tipo


class refri(bebidas):
    def __init__(self,nome,tipo,temperatura):
        super().__init__(nome,tipo)
        self.temperatura = temperatura


class cafe(refri):
    def __init__(self,nome,tipo,temperatura,forma):
        super().__init__(nome,tipo,temperatura)
        self.forma = forma


refrigerante = refri('coca-cola','refrigerante','gelado')
print(refrigerante.temperatura)

cafezinho = cafe('café','mesclado','quente','maquina')
print(cafezinho.forma)

