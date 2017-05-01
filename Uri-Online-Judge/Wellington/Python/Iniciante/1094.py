# -*- coding: utf-8 -*-

cobaias = {'R': 0, 'S': 0, 'C': 0}

n = input()

for x in range(n):
	linha = raw_input().split(' ')
	cobaias[linha[1]] += int(linha[0])

total = cobaias['R'] + cobaias['S'] + cobaias['C']
pCoelhos = (100.0 * cobaias['C'])/total #formula para saber o percentual do coelho sobre o total
pRatos = (100.0 * cobaias['R'])/total
pSapos = (100.0 * cobaias['S'])/total

print("Total: %i cobaias" % total)
print("Total de coelhos: %i" % cobaias['C'])
print("Total de ratos: %i" % cobaias['R'])
print("Total de sapos: %i" %cobaias['S'])
print("Percentual de coelhos: %.2f " % pCoelhos + str("%"))
print("Percentual de ratos: %.2f " % pRatos + str("%"))
print("Percentual de sapos: %.2f " % pSapos + str("%"))