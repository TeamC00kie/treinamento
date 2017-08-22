# -*- coding: utf-8 -*-

linha = list(map(int, input().split()))

a, b, c = linha

maiorAB = int((a + b + abs(a-b))/2)
maior = int((maiorAB + c + abs(maiorAB - c))/2)

print('{} eh o maior'.format(maior))