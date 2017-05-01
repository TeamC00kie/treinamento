# -*- coding: utf-8 -*-

valor = input() #ler valor

print(valor)
print(str(valor / 100) + " nota(s) de R$ 100,00") #divisão de inteiros vai resultar em um numero inteiro
valor %= 100 #para pegar o resto da divisão/dinheiro que sobrou
print(str(valor / 50) + " nota(s) de R$ 50,00")
valor %= 50
print(str(valor / 20) + " nota(s) de R$ 20,00")
valor %= 20
print(str(valor / 10) + " nota(s) de R$ 10,00")
valor %= 10
print(str(valor / 5) + " nota(s) de R$ 5,00")
valor %= 5
print(str(valor / 2) + " nota(s) de R$ 2,00")
valor %= 2
print(str(valor) + " nota(s) de R$ 1,00")