# -*- coding: utf-8 -*-

item = [4.00, 4.50, 5.00, 2.00, 1.50]

linha = raw_input().split(' ') #ler valores
c, q = linha #array para variaveis
c = int(c) - 1 #-1 pq o codigo vai de 1 a 5 e o vetor de 0 a 4
q = int(q)

total = item[c] * q #calculo

print("Total: R$ %.2f" % (total)) #imprime com 2 casas decimais 