class Resto:
    def __init__(self, numero):
        self.numero = numero
        self.resto = 0

    def calcular_resto(self):
        self.resto = self.numero % 2
        return self.resto

    def imprimir_resto(self):
        if self.resto == 0:
            print("O número {} é par".format(self.numero))
        else:
            print("O número {} é impar".format(self.numero))
