class veiculo:
    def __init__(self, modelo, ano, marca):
        self.modelo = modelo
        self.ano = ano
        self.marca = marca

class carro2(veiculo):
    def __init__(self,modelo,ano,marca,portas):
        super().__init__(modelo,ano,marca)
        self.portas = portas

class moto(veiculo):
    def __init__(self,modelo,marca,ano,guidao):
        super().__init__(modelo,marca,ano)
        self.guidao = guidao


carrinho = carro2('citroen','ford',2000,4)

print(carrinho.modelo,carrinho.ano,carrinho.marca,carrinho.portas)

moto = moto('harley','honda',2019,'vermelho')
print(moto.modelo,moto.ano,moto.marca,moto.guidao)
