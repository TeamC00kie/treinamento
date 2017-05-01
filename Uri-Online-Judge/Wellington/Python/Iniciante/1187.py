# -*- coding: utf-8 -*-

m = []

operacao = raw_input()

for i in range(12):
	m.append([])
	for j in range(12):
		m[i].append(input())

soma = 0
media = 0
cont = 0.0
a = 11
b = 1
for i in range(5):
	j = b
	while j < a:
		soma += m[i][j]
		j += 1
		cont += 1
	a -= 1
	b += 1

if operacao == "S":
	print("%.1f" % soma)
else:
	media = soma / cont
	print("%.1f" % media)