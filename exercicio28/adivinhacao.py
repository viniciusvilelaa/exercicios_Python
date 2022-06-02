from random import randint


print("Vou pensar em um numero entre 0 e 5. Tente adivinhar...")
numero_secreto = int(input("Em que numero eu pensei? "))
numero = randint(0, 5)
if numero == numero_secreto:
    print("Parabens! Você acertou!")
else:
    print("Você errou! Eu pensei no numero {}".format(numero))