# -*- coding: utf-8 -*-
import sys

while True:
	try:
		input()
		v = map(int, raw_input().split())
		v.sort(reverse=True)
		if v[0] < 10:
			print(1)
		elif v[0] < 20:
			print(2)
		else:
			print(3)
			
	except EOFError:
		break