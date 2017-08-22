# -*- coding: utf-8 -*-

linha = list(map(float, input().split()))
a, b, c = linha

if abs(b-c) < a and a < b+c and abs(a-c) < b and b < a+c and abs(a-b) < c and c < a+b:
	print('Perimetro = {:.1f}'.format(a+b+c))
else:
	print('Area = {:.1f}'.format((c * (a + b))/2))