# -*- coding: utf-8 -*-

n = input() #ler valor

hora = n / 3600 #minutos * hora = 3600
n %= 3600
minuto = n / 60
n %= 60
segundo = n

print("%i:%i:%i" % (hora,minuto,segundo)) #imprimir tempo