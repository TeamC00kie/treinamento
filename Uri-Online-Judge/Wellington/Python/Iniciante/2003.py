# -*- coding: utf-8 -*-

while True:
	try:
		hora = map(int, raw_input().split(":"))
		atraso = 0
		if hora[0] >= 7:
			hora[0] -= 7
			atraso = (hora[0] * 60) + hora[1]
		else:
			atraso = 0

		print("Atraso maximo: %i" % atraso)
	except EOFError:
		break