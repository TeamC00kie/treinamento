# -*- coding: utf-8 -*-

jogos = 0
inter = 0
gremio = 0
empates = 0

while True:
	linha = raw_input().split(" ")
	linha[0] = int(linha[0])
	linha[1] = int(linha[1])

	#Saber quem ganhou ou se empatou
	if linha[0] == linha[1]:
		empates += 1
	elif linha[0] > linha[1]:
		inter += 1
	elif linha[0] < linha[1]:
		gremio += 1
	jogos += 1

	#Se vai existe outro jogo
	condicao = 1
	while True:
		print("Novo grenal (1-sim 2-nao)")
		condicao = input()
		if condicao == 1 or condicao == 2:
			break

	#Caso a resporta seja 2 ele vai parar a execução do while
	if condicao == 2:
		break

#resultados
print("%i grenais" % jogos)
print("Inter:%i" % inter)
print("Gremio:%i" % gremio)
print("Empates:%i" % empates)
#saber quem ganhou mais
if inter == gremio:
	print("Nao houve vencedor")
elif inter > gremio:
	print("Inter venceu mais")
elif inter < gremio:
	print("Gremio venceu mais")