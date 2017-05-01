# -*- coding: utf-8 -*-

idade = input() #ler idade em dias

ano = idade / 365 #calculo
idade %= 365
mes = idade / 30
idade %= 30
dia = idade

print("%i ano(s)" % ano) #imprimir
print("%i mes(es)" % mes)
print("%i dia(s)" % dia)