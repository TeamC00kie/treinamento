# -*- coding: utf-8 -*-

n = input()

for i in range(n):
	x = input()

	cont = 0

	for j in range(1, x + 1):
		if x % j == 0:
			cont += 1

	if cont == 2:
		print("%i eh primo" % x)
	else: 
		print("%i nao eh primo" % x)