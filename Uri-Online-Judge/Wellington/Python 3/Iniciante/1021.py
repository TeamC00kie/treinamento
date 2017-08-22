# -*- coding: utf-8 -*-

n = float(input())
notas = int(n)
moedas = int((n-notas)*100)

print('NOTAS:')
print('{} nota(s) de R$ 100.00'.format(int(notas/100)))
notas %= 100
print('{} nota(s) de R$ 50.00'.format(int(notas/50)))
notas %= 50
print('{} nota(s) de R$ 20.00'.format(int(notas/20)))
notas %= 20
print('{} nota(s) de R$ 10.00'.format(int(notas/10)))
notas %= 10
print('{} nota(s) de R$ 5.00'.format(int(notas/5)))
notas %= 5
print('{} nota(s) de R$ 2.00'.format(int(notas/2)))
notas %= 2

print('MOEDAS:')
#Apesar do 1 ser uma moeda ele ainda é um número inteiro
print('{} moeda(s) de R$ 1.00'.format(int(notas)))
print('{} moeda(s) de R$ 0.50'.format(int(moedas/50)))
moedas %= 50
print('{} moeda(s) de R$ 0.25'.format(int(moedas/25)))
moedas %= 25
print('{} moeda(s) de R$ 0.10'.format(int(moedas/10)))
moedas %= 10
print('{} moeda(s) de R$ 0.05'.format(int(moedas/5)))
moedas %= 5
print('{} moeda(s) de R$ 0.01'.format(int(moedas)))