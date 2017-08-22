# -*- coding: utf-8 -*-

linha = list(map(int, input().split()))
a, b = linha

if a % b == 0 or b % a == 0:
	print('Sao Multiplos')
else:
	print('Nao sao Multiplos')