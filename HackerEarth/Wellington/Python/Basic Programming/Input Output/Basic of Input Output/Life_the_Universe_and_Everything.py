# -*- coding: utf-8 -*-

x = []
while True:
	x.append(input())
	if x[len(x) - 1] == 42:
		break
for i in range(len(x) - 1):
	print(x[i])