import random

lista_alunos = []

lista_alunos.append(input('Nome do primeiro aluno: '))
lista_alunos.append(input('Nome do segundo aluno: '))
lista_alunos.append(input('Nome do terceiro aluno: '))
lista_alunos.append(input('Nome do quarto aluno: '))

escolhido = random.choice(lista_alunos)

print("O aluno escolhido foi {}".format(escolhido))