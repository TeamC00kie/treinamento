# -*- coding: utf-8 -*-

while True:
	
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

	condicao = 1
	while True:
		print("novo calculo (1-sim 2-nao)")
		condicao = input()
		if condicao == 2 or condicao == 1:
			break

	if condicao == 2:
		break