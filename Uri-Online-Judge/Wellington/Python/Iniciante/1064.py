# -*- coding: utf-8 -*-

positivos = 0
media = 0.0
for x in range(6):
	numero = input()
	if numero > 0:
		positivos += 1
		media += numero

media /= positivos

print("%i valores positivos" % positivos)
print("%.1f" % media)