# -*- coding: utf-8 -*-
import sys

while(True):
	try:
		n = input()
		um = n/3
		dois = 0
		tres = n - 1
		for i in range(n):
			for j in range(n):
				if dois == tres and dois == j and dois == i:
					print(4),
					sys.stdout.write("")
				elif j >= um and i >= um and i <= (n - 1) - um and j <= (n - 1) - um:
					print(1),
					sys.stdout.write("")
				elif j == dois:
					print(2),
					sys.stdout.write("")
				elif j == tres:
					print(3),
					sys.stdout.write("")
				else:
					print(0),
					sys.stdout.write("")
			dois += 1
			tres -= 1
			print("")
		print("")
	except EOFError:
		break