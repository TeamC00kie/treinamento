# -*- coding: utf-8 -*-

input()

t = map(int, raw_input().split())

menor = 0
posicao = 0
for x in range(len(t)):
	if x == 0:
		menor = t[x]
		posicao = x + 1
	if menor > t[x]:
		menor = t[x]
		posicao = x + 1

print(posicao)