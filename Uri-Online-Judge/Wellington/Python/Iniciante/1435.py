# -*- coding: utf-8 -*-
import sys

while True:
	n = input()
	if n == 0:
		break

	m = []

	for i in range(n):
		m.append([])
		for j in range(n):
			aux = [i+1, j+1, n-i, n-j]
			aux.sort()

			m[i].append(aux[0])


			if j == n - 1 and j == 0:
				print("  %i" % m[i][j])
			elif j == n - 1:
				print("   %i" % m[i][j])
			elif j == 0:
				print("  %i" % m[i][j]),
				sys.stdout.write("")
			elif aux[0] < 10:
				print("   %i" % m[i][j]),
				sys.stdout.write("")
			elif aux[0] >= 10:
				print("  %i" % m[i][j]),
				sys.stdout.write("")

	print("")