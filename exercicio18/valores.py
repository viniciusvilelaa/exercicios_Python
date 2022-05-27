import math

class Valores:
    def __init__(self,angulo):
        self.angulo = angulo
        self.seno = None
        self.cos = None
        self.tan = None

    def Calcular(self):
        self.seno = math.sin(math.radians(self.angulo))
        self.cos = math.cos(math.radians(self.angulo))
        self.tan = math.tan(math.radians(self.angulo))
        print("O angulo de {} tem o SENO de {:.2F}".format(self.angulo,self.seno))
        print("O angulo de {} tem o COSSENO de {:.2F}".format(self.angulo,self.cos))
        print("O angulo de {} tem a TANGENTE de {:.2F}".format(self.angulo,self.tan))