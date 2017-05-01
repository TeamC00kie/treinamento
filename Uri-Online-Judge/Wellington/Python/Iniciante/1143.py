# -*- coding: utf-8 -*-
import sys

n = input()

for x in range(1, n + 1):
	for i in range(1,4):
		if i != 3:
			print("%i " % (x ** i)),
			sys.stdout.write("")
		else:
			print("%i" % (x ** i))