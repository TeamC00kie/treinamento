# -*- coding: utf-8 -*-
import sys

while True:
	x = input()
	
	if x == 0:
		break

	for i in range(1, x + 1):
		if i != x:
			print("%i " % i),
			sys.stdout.write("")
		else:
			print("%i" % i)