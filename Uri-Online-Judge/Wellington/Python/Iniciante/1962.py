# -*- coding: utf-8 -*-

n = input()

for x in range(n):
	t = input()
	c = ""
	if t >= 2015:
		anos = abs(2015 - t) + 1
		c = "A.C."
	else:
		anos = abs(2015 - t)
		c = "D.C."
	print("%i " % anos + c)