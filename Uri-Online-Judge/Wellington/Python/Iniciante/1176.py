# -*- coding: utf-8 -*-

fib = []

t = input()

for x in range(61):
	if x == 0:
		fib.append(0)
	elif x == 1:
		fib.append(1)
	else:
		fib.append(fib[x-2] + fib[x-1])

for x in range(t):
	posicao = input()
	print("Fib(%i) = %i" % (posicao, fib[posicao]))