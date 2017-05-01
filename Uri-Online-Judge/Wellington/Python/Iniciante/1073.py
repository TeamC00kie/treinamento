# -*- coding: utf-8 -*-

n = input()

for x in range(2,n+1):
	if x % 2 == 0:
		print("%i^2 = %i" % (x, x**2))