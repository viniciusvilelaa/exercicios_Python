from passagem import Passagem

kilometragem = float(input("Qual é a distancia da sua viagem? "))
passagem = Passagem(kilometragem)
passagem.calcular_valor()
passagem.imprimir_valor()