# -*- coding: utf-8 -*-

n = input()
r = map(int, raw_input().split(" "))
queda = 0
caido = False

for i in range(n):
	if i != 0:
		if r[i] < r[i - 1] and not caido:
			queda = i + 1
			caiu = True
			break

print(queda)