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
			aux = abs(i - j) + 1

			m[i].append(aux)


			if j == n - 1 and aux == 100:
				print(" %i" % m[i][j])
			elif j == n - 1 and j == 0 or j == n - 1 and aux >= 10:
				print("  %i" % m[i][j])
			elif j == n - 1:
				print("   %i" % m[i][j])
			elif j == 0 and aux < 10:
				print("  %i" % m[i][j]),
				sys.stdout.write("")
			elif j == 0 and aux == 100:
				print("%i" % m[i][j]),
				sys.stdout.write("")
			elif j == 0 and aux >= 10:
				print(" %i" % m[i][j]),
				sys.stdout.write("")
			elif aux < 10:
				print("   %i" % m[i][j]),
				sys.stdout.write("")
			elif aux >= 10:
				print("  %i" % m[i][j]),
				sys.stdout.write("")

	print("")