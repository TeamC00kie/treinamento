# -*- coding: utf-8 -*-

salario = input()
percentual = 0

if salario <= 400: #condições
	percentual = 0.15
elif salario <= 800:
	percentual = 0.12
elif salario <= 1200:
	percentual = 0.10
elif salario <= 2000:
	percentual = 0.07
else:
	percentual = 0.04

reajuste = salario * percentual #calcula reajuste

print("Novo salario: %.2f" % (reajuste + salario))
print("Reajuste ganho: %.2f" % reajuste)
print("Em percentual: %.0f " % (percentual * 100) + str("%")) #% é um operador por isso a conversão para string