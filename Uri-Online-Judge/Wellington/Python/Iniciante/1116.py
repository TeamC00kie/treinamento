# -*- coding: utf-8 -*-

n = input()

for x in range(n):
	linha = raw_input().split(" ")
	linha[0] = float(linha[0])
	linha[1] = float(linha[1])

	divisao = 0.0
	if linha[1] != 0:
		divisao = linha[0] / linha[1]
		print("%.1f" % divisao)
	else:
		print("divisao impossivel")