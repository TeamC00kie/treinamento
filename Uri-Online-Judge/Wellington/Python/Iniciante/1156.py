# -*- coding: utf-8 -*-

x = 1.0
y = 1.0
s = 0.0
while True:
	s += x/y
	x += 2
	y *= 2
	if x > 39:
		break
	

print("%.2f" % s)