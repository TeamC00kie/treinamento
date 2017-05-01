# -*- coding: utf-8 -*-

x = input()
y = 0
while True:
	y = input()
	if y > x:
		break

valores = 0
soma = 0
while True:
	if soma > y:
		break

	soma += x
	x += 1
	valores += 1

print(valores)