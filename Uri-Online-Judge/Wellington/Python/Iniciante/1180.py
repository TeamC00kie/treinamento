# -*- coding: utf-8 -*-

n = input()
menor = 0
posicao = 0

x = map(int, raw_input().split())

for i in range(len(x)):
	if min(x) == x[i]:
		posicao = i

print("Menor valor: %i" % min(x))
print("Posicao: %i" % posicao)