# -*- coding: utf-8 -*-

produtos = {1001:1.5, 1002:2.5, 1003:3.5, 1004:4.5, 1005:5.5}

n = input()

total = 0

for x in range(n):
	entrada = map(float, raw_input().split())
	total += produtos[int(entrada[0])] * entrada[1]

print("%.2f" % total)