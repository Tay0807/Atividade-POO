class conta_bancaria:
    def calcular_juros(self,a):
        pass

class conta_poupanca(conta_bancaria):
    def calcular_juros(self,a):
        print(a*0.1)

class conta_corrente(conta_bancaria):
    def calcular_juros(self,a):
        print(a*0.3)


poupanca = conta_poupanca()
poupanca.calcular_juros(200)

corrente = conta_corrente()
corrente.calcular_juros(200)

