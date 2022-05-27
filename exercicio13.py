salario = float(input("Qual é o salario do funcionário? R$"))

REAJUSTE = salario * 0.15

salario_novo = salario + REAJUSTE

print("Um funcionario que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}".format(salario, salario_novo))