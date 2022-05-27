class Aluguel:
    def __init__(self,dias,km):
        self.dias = dias
        self.km = km
        self.preço_dia = float(60)
        self.preço_km = float(0.15)
        self.total = None
    
    def total_pagar(self):
        self.total = (self.preço_dia * self.dias) + (self.preço_km * self.km)
        print("O total a pagar é de R${}".format(self.total))