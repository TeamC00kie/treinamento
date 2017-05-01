# -*- coding: utf-8 -*-

valores = raw_input().split(' ')
valores[0] = float(valores[0]) #converte valores
valores[1] = float(valores[1])
valores[2] = float(valores[2])
valores.sort(reverse=True) #ordena em ordem decrescente

if valores[0] >= valores[1] + valores[2]: #condições
	print('NAO FORMA TRIANGULO')
else:
	if valores[0] ** 2 == valores[1] ** 2 + valores[2] ** 2:
		print('TRIANGULO RETANGULO')
	if valores[0] ** 2 > valores[1] ** 2 + valores[2] ** 2:
		print('TRIANGULO OBTUSANGULO')
	if valores[0] ** 2 < valores[1] ** 2 + valores[2] ** 2:
		print('TRIANGULO ACUTANGULO')
	if valores[0] == valores[1] and valores[0] == valores[2]:
		print('TRIANGULO EQUILATERO')
	if valores[0] == valores[1] and valores[0] != valores[2] or valores[0] == valores[2] and valores[0] != valores[1] or valores[1] == valores[2] and valores[1] != valores[0]:
		print('TRIANGULO ISOSCELES')