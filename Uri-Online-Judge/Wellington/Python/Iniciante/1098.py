# -*- coding: utf-8 -*-

i = 0
j = 1
n = 3

while i <= 2:
	i = round(i, 1)
	if i == 0 or i == 1 or i == 2:
		print("I=%.0f J=%.0f" % (i, j))
	else:
		print("I=%.1f J=%.1f" % (i, j))
	
	j += 1
	if j > n:
		i += 0.2
		n += 0.2
		j = i + 1