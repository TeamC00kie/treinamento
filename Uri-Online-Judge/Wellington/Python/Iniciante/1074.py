# -*- coding: utf-8 -*-

n = input()

for x in range(n):
	entrada = input()
	if entrada == 0:
		print("NULL")
	if entrada % 2 == 0 and entrada != 0:
		print("EVEN"),
	elif entrada % 2 != 0 and entrada != 0: 
		print("ODD"),
	if entrada > 0:
		print("POSITIVE")
	elif entrada < 0:
		print("NEGATIVE")