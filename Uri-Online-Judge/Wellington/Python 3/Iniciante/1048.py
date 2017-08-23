# -*- coding: utf-8 -*-

salario = float(input())

if (salario <= 400):
	percentual = 15
elif (salario <= 800):
	percentual = 12
elif (salario <= 1200):
	percentual = 10
elif (salario <= 2000):
	percentual = 7
else:
	percentual = 4

reajuste = salario * (percentual/100)
novoSalario = salario + reajuste

print('Novo salario: {:.2f}'.format(novoSalario))
print('Reajuste ganho: {:.2f}'.format(reajuste))
print('Em percentual: {} %'.format(percentual))