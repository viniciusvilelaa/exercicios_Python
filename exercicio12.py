preço = float(input("Qual é o preço do produto? R$"))

desc = preço * 0.05

preço_final = preço - desc

print("O produto que custava R${}, na promoção com desconto de 5% vai custar R${:.2f}".format(preço, preço_final))