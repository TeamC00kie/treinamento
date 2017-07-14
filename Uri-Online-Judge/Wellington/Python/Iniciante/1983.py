# -*- coding: utf-8 -*-

n = input()
matricula = 0
nota = 0

for x in range(n):
	entrada = map(float, raw_input().split())
	if entrada[1] > nota:
		matricula = entrada[0]
		nota = entrada[1]

if nota >= 8:
	print(int(matricula))
else:
	print("Minimum note not reached")