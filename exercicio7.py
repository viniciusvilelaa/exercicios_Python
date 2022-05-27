from tokenize import Double


primeira_nota = float(input("Digite a primeira nota: "))
segunda_nota = float(input("Digite a segunda nota: "))

media = (primeira_nota + segunda_nota) / 2

print("A media entre {} e {} é igual a: {} ".format(primeira_nota, segunda_nota, media))