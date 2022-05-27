largura = float(input("Digite o valor da Largura: "))
altura = float(input("Digite o valor da Altura: "))

area = largura * altura

litros_tinta = area / 2

print("Sua parede tem a dimensão de {} x {} e sua área é de {}m²".format(largura, altura, area))
print("Para pintar essa parede, você precisará de {}l de tinta.".format(litros_tinta))


