# -*- coding: utf-8 -*-

x = input()

print("N[0] = %i" % x)
for i in range(1,10):
	print("N[%i] = %i" % (i, x * 2))
	x *= 2