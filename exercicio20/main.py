import random

lista_alunos = []

lista_alunos.append(input('Nome do primeiro aluno: '))
lista_alunos.append(input('Nome do segundo aluno: '))
lista_alunos.append(input('Nome do terceiro aluno: '))
lista_alunos.append(input('Nome do quarto aluno: '))

ordem = random.sample(lista_alunos,4)

print("A ordem de apresentação será: {}".format(ordem))