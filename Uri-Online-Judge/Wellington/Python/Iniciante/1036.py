# -*- coding: utf-8 -*-

import math

linha = raw_input().split(' ') #ler valores
a, b, c = linha #array para variaveis
a = float(a) #converte valores
b = float(b)
c = float(c)

delta = pow(b, 2) - 4 * a * c #calcula delta

if a != 0 and delta > 0: #condição para calculo
	r1 = (-b + math.sqrt(delta)) / (2 * a)
	r2 = (-b - math.sqrt(delta)) / (2 * a)

	print('R1 = %.5f' % r1)
	print('R2 = %.5f' % r2)

else: #não pode ser calculado 
	print('Impossivel calcular')