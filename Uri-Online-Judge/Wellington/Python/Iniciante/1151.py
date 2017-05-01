# -*- coding: utf-8 -*-
import sys

n = input()
anterior = 1
fib = 0

for x in range(n):
	if x != n - 1:
		print("%i " % fib),
		sys.stdout.write("")
		aux = fib
		fib += anterior
		anterior = aux
	else:
		print(fib)