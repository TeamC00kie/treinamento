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
meio = False
um = False
a = 10
for i in range(1,11):
	j = 11
	while j > a:
		soma += m[i][j]
		j -= 1
		cont += 1

	if a == 6 and not um:
		meio = True
		a -= 1
		um = True
	if meio:
		a += 1
	else:
		a -= 1
	

if operacao == "S":
	print("%.1f" % soma)
else:
	media = soma / cont
	print("%.1f" % media)