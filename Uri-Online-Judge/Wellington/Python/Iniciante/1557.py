# -*- coding: utf-8 -*-
import sys

while(True):
	n = input()
	if n == 0:
		break
	vetor  = []
	aux = 0
	for i in range(n):
		vetor.append([])
		for j in range(n):
			s = 0
			if i == 0 and j == 0:
				s = 1
			else:
				s = 2 ** (j+aux)
			vetor[i].append(s)
		aux += 1

	tamanho = vetor[n - 1][n - 1]
	tamanho = len(str(tamanho)) + 1
	tamanhoP = vetor[n - 1][0]
	tamanhoP = len(str(tamanhoP)) + 1

	for i in range(n):
		for j in range(n):
			if j == 0 and n <= 2:
				espaco = " " * ((tamanhoP - 1) - len(str(vetor[i][j])))
			elif j == 0:
				espaco = " " * ((tamanho - 1) - len(str(vetor[i][j])))
			else:
				espaco = " " * (tamanho-len(str(vetor[i][j])))

			print(espaco + str(vetor[i][j])),
			sys.stdout.write("")
		print("")
	print("")