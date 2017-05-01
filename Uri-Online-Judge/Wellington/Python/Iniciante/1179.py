# -*- coding: utf-8 -*-

impar = []
par = []

def imprimir(isPar):
	if isPar:
		for x in range(len(par)):
			print("par[%i] = %i" % (x, par[x]))
		for x in range(len(par)):
			del par[0]
	else:
		for x in range(len(impar)):
			print("impar[%i] = %i" % (x, impar[x]))
		for x in range(len(impar)):
			del impar[0]

for x in range(15):
	entrada = input()
	if entrada % 2 == 0:
		par.append(entrada)
		if len(par) == 5:
			imprimir(True)
	else:
		impar.append(entrada)
		if len(impar) == 5:
			imprimir(False)

if len(impar) != 0:
	imprimir(False)
if len(par) != 0:
	imprimir(True)