# -*- coding: utf-8 -*-

n = input()

for j in range(n):
	linha = raw_input().split(" ")
	linha[0] = int(linha[0])
	linha[1] = int(linha[1])
	linha.sort()
	x, y = linha
	soma = 0

	for i in range(x + 1, y):
		if i % 2 != 0:
			soma += i

	print(soma)