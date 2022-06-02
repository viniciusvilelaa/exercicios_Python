from classes import Multa

km = float(input("Qual a velocidade atual do carro? "))
multa = Multa(km)

if km > 80:
    multa.Calcular()
else:
    print("Tenha um bom dia! Dirija com segurança!")