# -*- coding: utf-8 -*-
import sys

t = input()

for x in range(t):
	assento = input()

	frente = 1
	mod = assento % 12
	if mod == 0:
		mod = 12
	aux = mod - 6
	primeiro = True
	if aux <= 0:
		primeiro = True
		aux = abs(aux)
	else:
		primeiro = False
		aux = abs(aux) - 1

	for x in range(aux):
		frente += 2

	if primeiro:
		frente += assento
	else:
		frente = assento - frente

	print(frente),
	sys.stdout.write("")

	if aux == 0 or aux == 5:
		print(" WS")
	elif aux == 1 or aux == 4:
		print(" MS")
	elif aux == 2 or aux == 3:
		print(" AS")