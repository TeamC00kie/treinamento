# -*- coding: utf-8 -*-

dinheiro = int(input())

print(dinheiro)
print('{} nota(s) de R$ 100,00'.format(int(dinheiro/100)))
dinheiro %= 100
print('{} nota(s) de R$ 50,00'.format(int(dinheiro/50)))
dinheiro %= 50
print('{} nota(s) de R$ 20,00'.format(int(dinheiro/20)))
dinheiro %= 20
print('{} nota(s) de R$ 10,00'.format(int(dinheiro/10)))
dinheiro %= 10
print('{} nota(s) de R$ 5,00'.format(int(dinheiro/5)))
dinheiro %= 5
print('{} nota(s) de R$ 2,00'.format(int(dinheiro/2)))
dinheiro %= 2
print('{} nota(s) de R$ 1,00'.format(int(dinheiro)))
