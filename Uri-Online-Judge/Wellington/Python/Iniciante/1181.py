# -*- coding: utf-8 -*-

m = []

linha = input()
operacao = raw_input()

for i in range(12):
	m.append([])
	for j in range(12):
		m[i].append(input())

soma = 0
media = 0
for i in range(12):
	soma += m[linha][i] 

if operacao == "S":
	print("%.1f" % soma)
else:
	media = soma / 12.0
	print("%.1f" % media)