# -*- coding: utf-8 -*-

n = int(input())
hora = int(n/3600)
minuto = int((n%3600)/60)
segundo = int((n%3600)%60)
print('{}:{}:{}'.format(hora, minuto, segundo))
