# -*- coding: utf-8 -*-

linha = raw_input().split(' ')
a, b = linha
a = int(a)
b = int(b)

if a % b == 0 or b % a == 0: #para saber se é multiplo
	print('Sao Multiplos')
else:
	print('Nao sao Multiplos')