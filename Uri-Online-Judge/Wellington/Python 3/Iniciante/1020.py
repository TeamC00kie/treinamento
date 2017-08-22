# -*- coding: utf-8 -*-

entradaDia = int(input())

ano = int(entradaDia/365)
print('{} ano(s)'.format(ano))
mes = int((entradaDia%365)/30)
print('{} mes(es)'.format(mes))
dia = int((entradaDia%365)%30)
print('{} dia(s)'.format(dia))