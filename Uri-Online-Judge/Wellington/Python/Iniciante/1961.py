# -*- coding: utf-8 -*-

entrada = raw_input().split()
p = int(entrada[0])
n = int(entrada[1])

canos = map(int, raw_input().split())

win = True
for x in range(1, n):
	altura = abs(canos[x-1] - canos[x])
	if altura > p:
		print("GAME OVER")
		win = False
		break

if win:
	print("YOU WIN")