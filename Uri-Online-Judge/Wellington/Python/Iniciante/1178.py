# -*- coding: utf-8 -*-

n = []
n.append(float(input()))

print("N[0] = %.4f" % n[0])
for x in range(1,100):
	n.append(n[x - 1] / 2)
	print("N[%i] = %.4f" % (x, n[x]))