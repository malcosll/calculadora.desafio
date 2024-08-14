class Soma:
    def __init__(self, a ,b):
        self.a = a 
        self.b = b

    def calcular(self):
        return self.a + self.b

class Mult:
    def __init__(self,a , b):
        self.a = a
        self.b = b

    def calcular(self):
        return self.a * self.b

class Div:
    def __init__(self, a ,b):
        self.a = a
        self.b = b

    def calcular(self):
        if self.b == 0:
            return "Erro: Divisão por zero!"

        return self.a % self.b
