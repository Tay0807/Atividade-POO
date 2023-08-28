class calculo:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def calcular(self,num1,num2):
        pass

class soma(calculo):
    def __init__(self,num1,num2):
        super().__init__(num1,num2)
    def calcular(self,num1,num2):
        print(self.num1+self.num2)

class subtracao(calculo):
    def __init__(self,num1,num2):
        super().__init__(num1,num2)
    def calcular(self,num1,num2):
        print(self.num1-self.num2)

class multiplica(calculo):
    def __init__(self,num1,num2):
        super().__init__(num1,num2)
    def calcular(self,num1,num2):
        print(self.num1*self.num2)

class dividir(calculo):
    def __init__(self,num1,num2):
        super().__init__(num1,num2)
    def calcular(self,num1,num2):
        print(self.num1/self.num2)


som = soma(2,8)
som.calcular(2,8)

subt = subtracao(9,8)
subt.calcular(9,8)

mult = multiplica(2,4)
mult.calcular(2,4)

div = dividir(8,2)
div.calcular(8,2)