# -*- coding: utf-8 -*-

linha = []
linha.append(input())
linha.append(input())
linha.sort()

soma = 0
for i in range(linha[0],linha[1] + 1):
	if i % 13 != 0:
		soma += i

print(soma)