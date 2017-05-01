# -*- coding: utf-8 -*-
import sys

while True:
	try:
		n = input()
		m = []

		um = 0
		dois = n - 1
		for i in range(n):
			m.append([])
			for j in range(n):
				if j == dois:
					m[i].append(2)
					print(m[i][j]),
					sys.stdout.write("")
				elif j == um:
					m[i].append(1)
					print(m[i][j]),
					sys.stdout.write("")
				else:
					m[i].append(3)
					print(m[i][j]),
					sys.stdout.write("")
			print("")
			um += 1
			dois -= 1

	except EOFError:
		break