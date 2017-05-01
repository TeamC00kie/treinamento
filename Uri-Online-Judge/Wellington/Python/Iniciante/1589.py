# -*- coding: utf-8 -*-

t = input()

for x in range(t):
	r = map(int, raw_input().split())
	conduite = r[0] + r[1]
	print(conduite)