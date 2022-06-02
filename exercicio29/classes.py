class Multa:
    def __init__(self,km):
        self.limite = 80
        self.km = km
        self.multa = 7
        self.total = None
    
    def Calcular(self):
        self.total = (self.km - self.limite) * self.multa
        print("\033[31mMULTADO! Você excedeu o limite permitido de {}Km/h\033[m".format(self.limite))
        print("\033[31mO valor da multa é de R$ {:.2F}\033[m".format(self.total))
        print("Tenha um bom dia! Dirija com segurança!")