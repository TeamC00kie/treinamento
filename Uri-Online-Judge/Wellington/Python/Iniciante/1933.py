# -*- coding: utf-8 -*-

cartas = map(int, raw_input().split())

if cartas[0] == cartas[1]:
	print(cartas[0])
elif cartas[0] > cartas[1]:
	print(cartas[0])
else:
	print(cartas[1])