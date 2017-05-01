# -*- coding: utf-8 -*-

pares = 0
for x in range(5):
	numero = input()
	if numero % 2 == 0:
		pares += 1

print("%i valores pares" % pares)