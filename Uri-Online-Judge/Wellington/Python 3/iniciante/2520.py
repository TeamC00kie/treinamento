while True:
	try:
		linha = input().split(' ')
		n, m = linha
		n = int(n)
		m = int(m)
		linhaAsh = 0
		colunaAsh = 0
		linhaPika = 0
		colunaPika = 0
		caminho = []

		for x in range(n):
			linha = input().split(' ')
			caminho.append(linha)
			for i in range(m):
				if caminho[x][i] == '1':
					colunaAsh = x
					linhaAsh = i
				if caminho[x][i] == '2':
					colunaPika = x
					linhaPika = i

		resultadoLinha = abs(linhaAsh - linhaPika)
		resultadoColuna = abs(colunaAsh - colunaPika)
		resultado = resultadoLinha + resultadoColuna

		print(resultado)
	except EOFError:
		break