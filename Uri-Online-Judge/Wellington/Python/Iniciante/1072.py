# -*- coding: utf-8 -*-

n = input()

dentro = 0
fora = 0
for x in range(n):
	numero = input()
	if numero >= 10 and numero <= 20:
		dentro += 1
	else:
		fora += 1

print("%i in" % dentro)
print("%i out" % fora)