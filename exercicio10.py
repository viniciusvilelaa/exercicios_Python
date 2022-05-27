dinheiro = float(input("Quanto dinheiro você tem na carteira: R$"))
DOLAR = 3.27

compra = dinheiro / DOLAR

print("Com {} você consegue comprar {:.2f} dolares!".format(dinheiro, compra))
