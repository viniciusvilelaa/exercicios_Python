from classes import Aluguel

dias = float(input("Quantos dias alugados? "))
km = float(input("Quantos Km rodados? "))

preço_aluguel = Aluguel(dias, km)

preço_aluguel.total_pagar()