# -*- coding: utf-8 -*-

t = input()

for x in range(t):
	n = input()
	s = list(raw_input())
	for i in range(n):
		decimal = ord(s[i])
		auxC = 99999
		auxD = 99999
		for j in range(decimal, 123):
			cont = 0
			for n in range(1, j + 1):
				if j % n == 0:
					cont += 1
			if cont == 2 and not(j >= 91 and j <= 96) and not(j <= 64):
				auxC = j
				break
		for j in range(decimal, 64, -1):
			cont = 0
			for n in range(1, j + 1):
				if j % n == 0:
					cont += 1
			if cont == 2 and not(j >= 91 and j <= 96) and not(j <= 64):
				auxD = j
				break

		crescente = abs(decimal - auxC)
		decrescente = abs(decimal - auxD)

		if crescente < decrescente:
			decimal = auxC
		else: 
			decimal = auxD
		
		s[i] = chr(decimal)

	s = "".join(s)
	print(s)