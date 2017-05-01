# -*- coding: utf-8 -*-

binario = {"---":0 ,"--*":1, "-*-":2, "-**":3, "*--":4, "*-*":5, "**-":6, "***":7}
gritos = 0

linha = []
soma = 0
while gritos < 3:
	entrada = raw_input()
	if entrada == "caw caw":
		linha.append(soma)
		soma = 0
		gritos += 1
	else:
		soma += binario[entrada]

for x in linha:
	print(x)