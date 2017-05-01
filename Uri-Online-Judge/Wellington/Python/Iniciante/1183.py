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
a = 1
for i in range(11):
	j = a
	while j < 12:
		soma += m[i][j]
		j += 1
		cont += 1
	a += 1

if operacao == "S":
	print("%.1f" % soma)
else:
	media = soma / cont
	print("%.1f" % media)