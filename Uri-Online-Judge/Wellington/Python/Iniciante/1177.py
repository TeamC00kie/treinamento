# -*- coding: utf-8 -*-

n = []
t = input()
cont = 0
for x in range(1000):
	if x % t == 0:
		cont = 0
	

	print("N[%i] = %i" % (x, cont))
	cont += 1