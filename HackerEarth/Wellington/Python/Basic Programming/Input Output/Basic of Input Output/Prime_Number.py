# -*- coding: utf-8 -*-
import sys

n = input()

for x in range(1,n + 1):
	cont = 0
	for i in range(1,x + 1):
		if x % i == 0:
			cont += 1

	if cont == 2:
		print(" %i" % x),
		sys.stdout.write("")
			
print("")