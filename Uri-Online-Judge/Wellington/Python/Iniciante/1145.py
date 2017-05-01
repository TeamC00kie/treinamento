# -*- coding: utf-8 -*-
import sys

linha = raw_input().split(" ")
x = int(linha[0])
y = int(linha[1])

for i in range(1, y + 1):
	if i % x != 0:
		print("%i " % i),
		sys.stdout.write("")
	else: 
		print("%i" % i)