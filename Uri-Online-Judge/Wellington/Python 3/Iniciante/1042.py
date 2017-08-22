# -*- coding: utf-8 -*-

numeros = list(map(int, input().split()))

ordenado = []

for aux in numeros:
	ordenado.append(aux)

ordenado.sort()
for aux in ordenado:
	print(aux)

print()

for aux in numeros:
	print(aux)