# -*- coding: utf-8 -*-

numero = []
maior = 0
posicao = 0
for x in range(100):
	numero.append(input())
	if x == 0:
		maior = numero[x]
		posicao = x + 1
	if maior < numero[x]:
		maior = numero[x]
		posicao = x + 1

print(maior)
print(posicao)