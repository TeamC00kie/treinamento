# -*- coding: utf-8 -*-

n = input()
fib = 1

for x in range(n):
	fib *= n - x

print(fib)