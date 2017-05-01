# -*- coding: utf-8 -*-

i = 1
j = 7
while j >= 5 and i <= 9:
	print("I=%i J=%i" % (i, j))
	j -= 1 
	if j == 4:
		i += 2
		j = 7