
class Temp:
    def __init__(self,temperatura):
        self.temperatura = temperatura
        self.f = None

    def converter(self):
        self.f = ((9*self.temperatura)/5) + 32
        print("A temperatura de {}°C corresponde a {}°F".format(self.temperatura,self.f))