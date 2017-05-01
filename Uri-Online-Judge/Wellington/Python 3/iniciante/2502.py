while True:
	try:
		linha = input().split(' ')
		c ,n = linha
		c = int(c)
		n = int(n)

		crip = input()
		crip = list(crip)
		descrip = input()
		descrip = list(descrip)
		frases = []

		for x in range(n):#0 até n-1
			frases.append(input())

		for x in range(n):#0 até quantidade de frases - 1
			frases[x] = list(frases[x])#fragmenta a frase
			for i in range(len(frases[x])):#0 até tamanho da frase - 1
				for p in range(c):
					if crip[p].lower() == frases[x][i]:
						frases[x][i] = descrip[p].lower()
						break
					elif crip[p].upper() == frases[x][i]:
						frases[x][i] = descrip[p].upper()
						break
					elif descrip[p].lower() == frases[x][i]:
						frases[x][i] = crip[p].lower()
						break
					elif descrip[p].upper() == frases[x][i]:
						frases[x][i] = crip[p].upper()
						break
			frases[x] = ''.join(frases[x])#faz a junção da frase
		for x in frases:
		    print(x)
		
		print()
	except EOFError:
		break