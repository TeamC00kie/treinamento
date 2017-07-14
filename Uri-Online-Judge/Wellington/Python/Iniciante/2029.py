# -*- coding: utf-8 -*-

while True:
	try:
		v = input()
		d = input()

		altura = v / (3.14 * pow(d / 2.0, 2))
		area = 3.14 * pow(d / 2.0, 2)

		print("ALTURA = %.2f" % altura)
		print("AREA = %.2f" % area)
	except EOFError:
		break