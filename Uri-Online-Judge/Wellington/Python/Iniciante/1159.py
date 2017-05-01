# -*- coding: utf-8 -*-

while True:
	x = input()

	if x == 0:
		break
		
	soma = 0
	for i in range(x, x + 10):
		if i % 2 == 0:
			soma += i

	print(soma)