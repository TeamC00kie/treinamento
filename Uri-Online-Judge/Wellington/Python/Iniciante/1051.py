# -*- coding: utf-8 -*-

salario = input()

imposto = 0
salario -= 2000 #para pegar só o valor que vai ser aplicado o imposto
if salario > 0: 
	if salario >= 1000: # se maior que 1000 ainda tem mais para cobrar o imposto
		imposto += 1000 * 0.08
	else: #se não for maior que 1000 acaba aqui o imposto 
		imposto += salario * 0.08

salario -= 1000
if salario > 0:
	if salario >= 1500:
		imposto += 1500 * 0.18
	else:
		imposto += salario * 0.18

salario -= 1500
if salario > 0:
	imposto += salario * 0.28

if imposto > 0:
	print("R$ %.2f" % imposto)
else: 
	print("Isento")