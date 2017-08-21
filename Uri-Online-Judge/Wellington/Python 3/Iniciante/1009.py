# -*- coding: utf-8 -*-

nome = input()
salario = float(input())
vendas = float(input())

salarioTotal = (vendas * 0.15) + salario

print('TOTAL = R$ {:.2f}'.format(salarioTotal))