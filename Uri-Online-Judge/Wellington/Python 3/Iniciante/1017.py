# -*- coding: utf-8 -*-

horas = int(input())
velocidade = int(input())

litros = (horas * velocidade)/12

print('{:.3f}'.format(litros))