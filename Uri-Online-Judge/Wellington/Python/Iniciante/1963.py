# -*- coding: utf-8 -*-

preco = map(float, raw_input().split())

crescimento = ((preco[1] - preco[0])/preco[0]) * 100

print("%.2f" % crescimento + "%")