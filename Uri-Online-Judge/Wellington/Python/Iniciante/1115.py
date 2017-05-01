# -*- coding: utf-8 -*-

while True:
	linha = raw_input().split(" ")
	linha[0] = int(linha[0])
	linha[1] = int(linha[1])

	if linha[0] == 0 or linha[1] == 0:
		break
	elif linha[0] > 0 and linha[1] > 0:
		print("primeiro")
	elif linha[0] < 0 and linha[1] > 0:
		print("segundo")
	elif linha[0] < 0 and linha[1] < 0:
		print("terceiro")
	elif linha[0] > 0 and linha[1] < 0:
		print("quarto")