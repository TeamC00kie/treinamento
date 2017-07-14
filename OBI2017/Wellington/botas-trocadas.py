# -*- coding: utf-8 -*-

def criarVetor():
	lista = []
	for x in range(30):
		lista.append(0)

	return lista

pares = 0
d = criarVetor()
e = criarVetor()

n = input()

for x in range(n):
	b = raw_input().split(" ")
	if b[1] == "D":
		d[int(b[0]) - 30] += 1
		if e[int(b[0]) - 30] > 0:
			e[int(b[0]) - 30] -= 1
			d[int(b[0]) - 30] -= 1
			pares += 1
	elif b[1] == "E":
		e[int(b[0]) - 30] += 1
		if d[int(b[0]) - 30] > 0:
			e[int(b[0]) - 30] -= 1
			d[int(b[0]) - 30] -= 1
			pares += 1

print(pares)