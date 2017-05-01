# -*- coding: utf-8 -*-

n = input() #ler valor

notas = int(n) #Apenas os valores inteiros
moedas = int((n - notas) * 100) #pegar valores apos a virgula

print("NOTAS:")
print("%i nota(s) de R$ 100.00" % (notas / 100)) #divisão de inteiros resulta em um inteiro
notas %= 100 #pegar o resto da divisão
print("%i nota(s) de R$ 50.00" % (notas / 50))
notas %= 50
print("%i nota(s) de R$ 20.00" % (notas / 20))
notas %= 20
print("%i nota(s) de R$ 10.00" % (notas / 10))
notas %= 10
print("%i nota(s) de R$ 5.00" % (notas / 5))
notas %= 5
print("%i nota(s) de R$ 2.00" % (notas / 2))
notas %= 2
print("MOEDAS:")
print("%i moeda(s) de R$ 1.00" % (notas)) #apesar de ser uma moeda ele ainda não está após a virgula
print("%i moeda(s) de R$ 0.50" % (moedas / 50))
moedas %= 50
print("%i moeda(s) de R$ 0.25" % (moedas / 25))
moedas %= 25
print("%i moeda(s) de R$ 0.10" % (moedas / 10))
moedas %= 10
print("%i moeda(s) de R$ 0.05" % (moedas / 5))
moedas %= 5
print("%i moeda(s) de R$ 0.01" % (moedas))