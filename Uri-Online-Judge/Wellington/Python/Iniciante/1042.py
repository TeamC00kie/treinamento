# -*- coding: utf-8 -*-

entrada = raw_input().split(' ')

ordenado = [] #cria vetor vazio

for x in entrada: #passa valores do vetor entrada para o ordenado no formato inteiro
	ordenado.append(int(x))

ordenado.sort() #ordena em ordem crescente

for x in ordenado: #imprime vetor
	print(x)

print('') #quebra de linha

for x in entrada: #imprime vetor
	print(x)