# -*- coding: utf-8 -*-
import sys

n = 1
while True:
	try:
		v = []
		x = input() + 1
		aux = 0

		for i in range(x):
			if i == 0:
				v.append(0)
			for j in range(aux):
				v.append(aux)
			aux += 1
		if x == 1:
			print("Caso %i: %i numero" % (n, len(v)))
		else:
			print("Caso %i: %i numeros" % (n, len(v)))
		for i in range(len(v)):
			if(i == len(v) - 1):
				print("%i\n" % v[i])
			else:
				print("%i " % v[i]),
				sys.stdout.write("")
		n += 1

	except EOFError:
		break