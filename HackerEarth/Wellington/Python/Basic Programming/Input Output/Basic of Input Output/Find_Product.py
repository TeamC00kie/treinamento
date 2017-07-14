# -*- coding: utf-8 -*-

n = input()
array = map(int, raw_input().split())

resposta = 1
for x in array:
	resposta = (resposta * x) % (10**9 + 7)

print(resposta)