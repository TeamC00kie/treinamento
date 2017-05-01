# -*- coding: utf-8 -*-
import math

while True:
	entrada = map(int, raw_input().split())
	if entrada[0] == 0:
		break

	area = float(entrada[0] * entrada[1])
	if entrada[2] == 100:
		truncar = math.sqrt(area)
		truncar = math.trunc(truncar)
		print(truncar)
	else:
		x = area * (entrada[2] / 100.0)
		areaX = area / x
		truncar = math.sqrt(areaX * area)
		truncar = math.trunc(truncar)
		print(truncar)