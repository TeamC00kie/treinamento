# -*- coding: utf-8 -*-

linha = list(map(float, input().split()))
a, b, c = linha

delta = b ** 2 - 4*a*c

if a != 0 and delta > 0:
	r1 = (-b + delta ** (1/2)) / (2 * a)
	r2 = (-b - delta ** (1/2)) / (2 * a)

	print('R1 = {:.5f}'.format(r1))
	print('R2 = {:.5f}'.format(r2))
else:
	print('Impossivel calcular')