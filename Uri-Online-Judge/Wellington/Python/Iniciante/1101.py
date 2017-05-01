# -*- coding: utf-8 -*-
import sys

while(True):
	linha = raw_input().split(" ")
	linha[0] = int(linha[0])
	linha[1] = int(linha[1])
	linha.sort()

	if linha[0] <= 0:
		break

	saida = ""

	soma = 0
	for x in range(linha[0], linha[1] + 1):
		if x == linha[1]:
			soma += x
			print("%i Sum=%i" % (x, soma))
		else:
			soma += x
			print("%i " % (x)),
			sys.stdout.write("")