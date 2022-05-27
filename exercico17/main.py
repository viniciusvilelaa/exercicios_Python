from hipotenusa import Hip

x = float(input("Comprimento do cateto oposto: "))
y = float(input("Comprimento do cateto adjacente: "))

hipo = Hip(x,y)

hipo.calcular()