# -*- coding: utf-8 -*-

linha = []
linha.append(input())
linha.append(input())
linha.sort()

soma = 0
for i in range(linha[0] + 1,linha[1]):
	if i % 5 == 2 or i % 5 == 3:
		print(i)