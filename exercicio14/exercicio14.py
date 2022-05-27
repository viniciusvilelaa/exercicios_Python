from temperatura import Temp

grau = float(input("Digite o valor em °C: "))

temp_base = Temp(grau)

temp_base.converter()
