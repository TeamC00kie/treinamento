# -*- coding: utf-8 -*-

import math #importação do math

linha1 = raw_input().split(' ') #ler valores na mesma linha
linha2 = raw_input().split(' ')

x1, y1 = linha1 #valores do array para variaveis
x2, y2 = linha2
x1 = float(x1) #conveter string para float
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)

distancia = math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2)) #sqrt = raiz and pow = potencia

print("%.4f" % distancia) #imprimir distancia com 4 casas decimais