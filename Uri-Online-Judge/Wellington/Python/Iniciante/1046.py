# -*- coding: utf-8 -*-

linha = raw_input().split(' ')
inicio, fim = linha
inicio = int(inicio)
fim = int(fim)

hora = fim - inicio 
if hora <= 0: #caso seja menor ou igual que 0 some com 24/ inicio=21 e fim=20 = -1 com +24 = 23
	hora += 24

print("O JOGO DUROU %i HORA(S)" % hora)