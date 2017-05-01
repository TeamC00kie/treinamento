# -*- coding: utf-8 -*-

a = []

for x in range(100):
	a.append(input())
for x in range(100):
	if a[x] <= 10:
		print("A[%i] = %.1f" % (x, a[x]))