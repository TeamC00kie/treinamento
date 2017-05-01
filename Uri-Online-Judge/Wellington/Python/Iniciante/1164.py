# -*- coding: utf-8 -*-

n = input()

for j in range(n):
	x = input()

	soma = 0
	for i in range(1, x):
		if x % i == 0:
			soma += i

	if x == soma:
		print("%i eh perfeito" % x)
	else:
		print("%i nao eh perfeito" % x)