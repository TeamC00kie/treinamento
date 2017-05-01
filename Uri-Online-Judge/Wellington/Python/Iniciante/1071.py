# -*- coding: utf-8 -*-

numero = []
numero.append(input())
numero.append(input())
numero.sort() #para o menor valor sempre ficar em primeiro

soma = 0
for x in range(numero[0]+1,numero[1]):
	if x % 2 != 0:
		soma += x

print(soma)