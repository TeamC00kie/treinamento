# -*- coding: utf-8 -*-

linha = raw_input().split(' ') #ler valores
a, b, c, d = linha #array para variaveis
a = int(a) #converte valores de string para int
b = int(b)
c = int(c)
d = int(d)

if b > c and d > a and c+d > a+b and c > 0 and d > 0 and a % 2 == 0: #testa condição
    print("Valores aceitos")
else:
    print("Valores nao aceitos")