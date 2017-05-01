# -*- coding: utf-8 -*-
import sys

n = input()
n *= 4
for x in range(1, n + 1):
	if x % 4 != 0:
		print("%i " % x),
		sys.stdout.write("")
	else:
		print("PUM")