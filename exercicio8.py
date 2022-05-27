medida_metro = float(input("Digite uma medida em metros: "))

km = medida_metro / 1000
mh = medida_metro / 100
dam = medida_metro / 10
dm = medida_metro * 10
cm = medida_metro * 100
mm = medida_metro * 1000


print("Km: {}".format(km))
print("Mh: {}".format(mh))
print("Dam: {}".format(dam))
print("Cm: {}".format(cm))
print("Mm: {}".format(mm))