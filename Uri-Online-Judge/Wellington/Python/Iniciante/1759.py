# -*- coding: utf-8 -*-
import sys

n = input()

for x in range(n):
	if x != n - 1:
		print("Ho "),
		sys.stdout.write("")
	else: 
		print("Ho!")