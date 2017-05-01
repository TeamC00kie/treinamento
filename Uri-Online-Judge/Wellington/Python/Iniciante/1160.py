# -*- coding: utf-8 -*-

t = input()

for x in range(t):
	linha = raw_input().split(" ")
	linha[0] = int(linha[0])
	linha[1] = int(linha[1])
	linha[2] = float(linha[2])
	linha[3] = float(linha[3])

	anos = 0

	while linha[0] <= linha[1]:
		linha[0] += int((linha[0] * linha[2]) / 100)
		linha[1] += int((linha[1] * linha[3]) / 100)
		anos += 1
		if anos > 100:
			break

	if anos <= 100:
		print("%i anos." % anos)
	else:
		print("Mais de 1 seculo.")