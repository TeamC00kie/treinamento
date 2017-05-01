# -*- coding: utf-8 -*-
import sys

t = input()

for x in range(t):
	entrada = raw_input().split()

	if entrada[0] == entrada[1]:
		print("Caso #%i: De novo!" % (x + 1))
	elif entrada[0] == "tesoura" and entrada[1] == "papel" or entrada[0] == "papel" and entrada[1] == "pedra" or entrada[0] == "pedra" and entrada[1] == "lagarto" or entrada[0] == "lagarto" and entrada[1] == "Spock" or entrada[0] == "Spock" and entrada[1] == "tesoura" or entrada[0] == "tesoura" and entrada[1] == "lagarto" or entrada[0] == "lagarto" and entrada[1] == "papel" or entrada[0] == "papel" and entrada[1] == "Spock" or entrada[0] == "Spock" and entrada[1] == "pedra" or entrada[0] == "pedra" and entrada[1] == "tesoura":
		print("Caso #%i: Bazinga!" % (x + 1))
	else:
		print("Caso #%i: Raj trapaceou!" % (x + 1))