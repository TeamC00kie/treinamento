# -*- coding: utf-8 -*-

x = input()

fim = 13
if x % 2 != 0:
	fim -= 1

for i in range(x,x+fim):
	if i % 2 != 0:
		print(i)