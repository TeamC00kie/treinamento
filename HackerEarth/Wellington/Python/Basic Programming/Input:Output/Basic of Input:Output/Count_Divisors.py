# -*- coding: utf-8 -*-

linha = map(int, raw_input().split())

cont = 0
for x in range(linha[0], linha[1] + 1):
	if x % linha[2] == 0:
		cont += 1
		
print(cont)