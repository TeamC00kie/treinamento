# -*- coding: utf-8 -*-

for j in range(2, 200):
	cont = 0
	for n in range(1, j + 1):
		if j % n == 0:
			cont += 1
	if cont == 2:
		print(j)