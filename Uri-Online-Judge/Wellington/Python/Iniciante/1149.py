# -*- coding: utf-8 -*-

linha = raw_input().split(" ")
a = int(linha[0])
n = int(linha[len(linha) - 1])

n += a
soma = 0
for x in range(a, n):
	soma += x

print(soma)