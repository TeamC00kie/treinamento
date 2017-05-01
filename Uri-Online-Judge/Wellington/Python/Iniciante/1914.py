# -*- coding: utf-8 -*-

q = input()

for x in range(q):
	nomes = raw_input().split()
	numeros = map(int, raw_input().split())
	soma = numeros[0] + numeros[1]

	if soma % 2 == 0:
		if nomes[1] == "PAR":
			print(nomes[0])
		else: 
			print(nomes[2])
	else:
		if nomes[1] == "IMPAR":
			print(nomes[0])
		else: 
			print(nomes[2])