# -*- coding: utf-8 -*-

positivo = 0

for x in range(6):
	numero = input()
	if numero > 0:
		positivo += 1

print("%i valores positivos" % positivo)