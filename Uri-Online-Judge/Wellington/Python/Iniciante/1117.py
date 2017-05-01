# -*- coding: utf-8 -*-

valores = []
while True:
	entrada = input()

	if entrada >= 0 and entrada <= 10:
		valores.append(entrada)
	else:
		print("nota invalida")

	if len(valores) == 2:
		media = (valores[0] + valores[1]) / 2.0
		print("media = %.2f" % media)
		break