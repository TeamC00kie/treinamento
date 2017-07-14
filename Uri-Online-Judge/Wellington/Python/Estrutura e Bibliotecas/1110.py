# -*- coding: utf-8 -*-

import sys #sem quebra de linha após o print

while True:
	n = input()
	if n == 0:
		break
	pilha = []
	descarte = []
	for x in range(1, n + 1):
		pilha.append(x)
	
	while len(descarte) != n - 1:
		descarte.append(pilha[0])
		del pilha[0]
		pilha.append(pilha[0])
		del pilha[0]
	print("Discarded cards:"),
	sys.stdout.write("")
	for x in range(n - 1):
		if x != 0:
			print(","),
			sys.stdout.write("")

		print(" %i" % descarte[x]),
		sys.stdout.write("")
	print("")
	print("Remaining card: %i" % pilha[0])