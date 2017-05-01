# -*- coding: utf-8 -*-

n = input()

for x in range(n):
	linha = raw_input().split(" ")
	linha[0] = int(linha[0])
	linha[1] = int(linha[1]) * 2

	soma = 0
	for x in xrange(linha[0], linha[0] + linha[1]):
		if x % 2 != 0:
			soma += x

	print(soma)