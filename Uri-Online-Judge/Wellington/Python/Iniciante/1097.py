# -*- coding: utf-8 -*-

i = 1
j = 7
n = 4
while i <= 9 and j >= 5:
	print("I=%i J=%i" % (i, j))
	j -= 1 
	if j == n:
		i += 2
		n += 2
		j = n + 3