# -*- coding: utf-8 -*-

n = input()

factorial = 1

for x in range(1, n + 1):
	factorial *= x

print(factorial)