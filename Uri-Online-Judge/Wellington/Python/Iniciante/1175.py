# -*- coding: utf-8 -*-

n = []

#recebe valores
for x in range(20):
	n.append(input())
#modifica valores
for x in range(10):
	aux = n[x]
	n[x] = n[(len(n) - 1) - x]
	n[(len(n) - 1) - x] = aux
#imprime valores
for x in range(20):
	print("N[%i] = %i" % (x, n[x]))