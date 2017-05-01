# -*- coding: utf-8 -*-

x = []

for i in range(10):
	x.append(input())
	if x[i] <= 0:
	 	x[i] = 1

for i in range(10):
	print("X[%i] = %i" % (i, x[i]))