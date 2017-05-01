# -*- coding: utf-8 -*-

linha = raw_input().split(' ') #ler valores
x, y = linha #vetor para variaveis
x = float(x) #converter para float
y = float(y)

if x > 0 and y > 0: #condições de saida
	print("Q1")
elif x < 0 and y > 0:
	print("Q2")
elif x < 0 and y < 0:
	print("Q3")
elif x > 0 and y < 0:
	print("Q4")
elif x == 0 and y != 0:
	print("Eixo Y")
elif x != 0 and y == 0:
	print("Eixo X")
else:
	print("Origem")