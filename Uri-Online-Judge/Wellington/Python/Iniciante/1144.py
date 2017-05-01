# -*- coding: utf-8 -*-
import sys

n = input()
segunda = False
x = 1

while x <= n:
	for i in range(1,4):
		if segunda:
			if i == 1:
				print("%i " % (x ** i)),
				sys.stdout.write("")
			elif i == 2:
				print("%i " % (x ** i + 1)),
				sys.stdout.write("")
			else:
				print("%i" % (x ** i + 1))
				segunda = False
				x += 1
		else:	
			if i != 3:
				print("%i " % (x ** i)),
				sys.stdout.write("")
			else:
				print("%i" % (x ** i))
				segunda = True