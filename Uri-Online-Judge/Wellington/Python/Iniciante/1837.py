# -*- coding: utf-8 -*-
import sys

entrada = map(int, raw_input().split())

if entrada[1] < 0:
	q = (entrada[0]/abs(entrada[1])) * - 1
	r = (entrada[0]%abs(entrada[1]))
else: 
	q = entrada[0]/entrada[1]
	r = entrada[0]%entrada[1]


print("%i %i" % (q, r))