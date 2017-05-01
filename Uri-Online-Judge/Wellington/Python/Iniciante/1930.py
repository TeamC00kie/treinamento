# -*- coding: utf-8 -*-

entrada = map(int, raw_input().split())

tomadas = 0
for x in range(len(entrada)):
	tomadas += entrada[x] - 1
tomadas += 1
print(tomadas)