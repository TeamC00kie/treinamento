# -*- coding: utf-8 -*-

linha1 = list(map(float, input().split()))
linha2 = list(map(float, input().split()))

x1, y1 = linha1
x2, y2 = linha2

distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1/2)

print('{:.4f}'.format(distancia))