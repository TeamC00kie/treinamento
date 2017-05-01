# -*- coding: utf-8 -*-

idade = []

while True:
	idade.append(input())
	if idade[len(idade) - 1] < 0:
		break

del idade[len(idade) - 1]
media = 0.0
for x in idade:
	media += x

media /= len(idade)

print("%.2f" % media)