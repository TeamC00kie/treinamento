# -*- coding: utf-8 -*-

l = input()
n = input()

for x in range(n):
	tamanho = map(int, raw_input().split())
	if tamanho[0] < l or tamanho[1] < l:
		print("UPLOAD ANOTHER")
	elif tamanho[0] == tamanho[1]:
		print("ACCEPTED")
	elif tamanho[0] >= l or tamanho >= tamanho[1]:
		print("CROP IT")