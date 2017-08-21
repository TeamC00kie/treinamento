# -*- coding: utf-8 -*-

linha1 = list(map(float, input().split()))
linha2 = list(map(float, input().split()))

total = (linha1[1] * linha1[2]) + (linha2[1] * linha2[2])

print('VALOR A PAGAR: R$ {:.2f}'.format(total))