while True:
	try:
		expressoes = []
		jogadores = []
		perdedores = []
		cont = 0
		t = int(input())

		for x in range(t):
			linha = input().replace('=',' ').split(' ')
			expressoes.append(linha)
		for x in range(t):
			linha = input().split(' ')
			jogadores.append(linha)

		for x in range(t):
			if jogadores[x][2] == '+' and int(expressoes[int(jogadores[x][1]) - 1][0]) + int(expressoes[int(jogadores[x][1]) - 1][1]) == int(expressoes[int(jogadores[x][1]) - 1][2]):
				cont += 1
			elif jogadores[x][2] == '-' and int(expressoes[int(jogadores[x][1]) - 1][0]) - int(expressoes[int(jogadores[x][1]) - 1][1]) == int(expressoes[int(jogadores[x][1]) - 1][2]):
				cont += 1
			elif jogadores[x][2] == '*' and int(expressoes[int(jogadores[x][1]) - 1][0]) * int(expressoes[int(jogadores[x][1]) - 1][1]) == int(expressoes[int(jogadores[x][1]) - 1][2]):
				cont += 1
			elif jogadores[x][2] == 'I' and not int(expressoes[int(jogadores[x][1]) - 1][0]) + int(expressoes[int(jogadores[x][1]) - 1][1]) == int(expressoes[int(jogadores[x][1]) - 1][2]) and not int(expressoes[int(jogadores[x][1]) - 1][0]) - int(expressoes[int(jogadores[x][1]) - 1][1]) == int(expressoes[int(jogadores[x][1]) - 1][2]) and not int(expressoes[int(jogadores[x][1]) - 1][0]) * int(expressoes[int(jogadores[x][1]) - 1][1]) == int(expressoes[int(jogadores[x][1]) - 1][2]):
				cont += 1
			else:
				perdedores.append(jogadores[x][0])

		if cont == 0:
			print('None Shall Pass!')
		elif cont == len(jogadores):
			print('You Shall All Pass!')
		else:
			perdedores.sort()
			perdedores = ' '.join(perdedores)
			print(perdedores)
	except EOFError:
		break