# -*- coding: utf-8 -*-

par = 0
impar = 0
positivo = 0
negativo = 0

for x in range(5):
	numero = input()
	if numero % 2 == 0:
		par += 1
	else:
		impar += 1
	if numero > 0:
		positivo += 1
	elif numero < 0:
		negativo += 1

print("%i valor(es) par(es)" % par)
print("%i valor(es) impar(es)" % impar)
print("%i valor(es) positivo(s)" % positivo)
print("%i valor(es) negativo(s)" % negativo)