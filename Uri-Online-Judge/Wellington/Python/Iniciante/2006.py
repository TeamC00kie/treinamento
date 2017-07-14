# -*- coding: utf-8 -*-

t = input()
p = map(int, raw_input().split())
cont = 0

for x in range(5):
	if p[x] == t:
		cont += 1

print(cont)