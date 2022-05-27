import math

class Hip:
    def __init__(self,x,y):
        self.co = x
        self.ad = y

    def calcular(self):
        self.hi = math.hypot(self.co,self.ad)
        print("A hipotenusa vai medir {:.2f}".format(self.hi))
