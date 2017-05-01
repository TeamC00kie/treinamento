# -*- coding: utf-8 -*-

while True:
	linha = raw_input().split(" ")
	linha[0] = int(linha[0])
	linha[1] = int(linha[1])

	if linha[0] == linha[1]:
		break
	elif linha[0] < linha[1]:
		print("Crescente")
	elif linha[0] > linha[1]:
		print("Decrescente")