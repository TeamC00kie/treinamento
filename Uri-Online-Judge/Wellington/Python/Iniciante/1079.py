# -*- coding: utf-8 -*-

n = input()

for x in range(n):
	linha = raw_input().split(' ')
	a, b, c = linha
	a = float(a) * 2
	b = float(b) * 3
	c = float(c) * 5
	media = (a + b + c)/10 
	print("%.1f" % media)