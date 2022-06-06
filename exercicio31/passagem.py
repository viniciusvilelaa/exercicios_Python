class Passagem:
    def __init__(self, kilometragem):
        self.km = kilometragem
        self.taxa1 = 0.5
        self.taxa2 = 0.45
        self.valor = None
    
    def calcular_valor(self):
        if self.km <= 200:
            self.valor = self.km * self.taxa1
        else:
            self.valor = 200 * self.taxa1 + (self.km - 200) * self.taxa2
    
    def imprimir_valor(self):
        print("Você esta prestes a começar uma viagem de {}Km".format(self.km))
        print("E o preço da sua passagem será de R${}".format(self.valor))