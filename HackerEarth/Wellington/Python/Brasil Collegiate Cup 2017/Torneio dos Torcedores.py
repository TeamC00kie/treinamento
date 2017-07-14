primeiro = map(int, raw_input().split())
primeiro.append(primeiro[0] + primeiro[1])
segundo = map(int, raw_input().split())
segundo.append(segundo[0] + segundo[1])
terceiro = map(int, raw_input().split())
terceiro.append(terceiro[0] + terceiro[1])
quarto = map(int, raw_input().split())
quarto.append(quarto[0] + quarto[1])

if(primeiro[2] >= segundo[2]):
	if(terceiro[2] > quarto[2]):
		if(primeiro[2] + quarto[1] >= terceiro[2] + segundo[1]):
			print 1
		else:
			print 3
	else:
		if(primeiro[2] + terceiro[1] >= quarto[2] + segundo[1]):
			print 1
		else:
			print 4
else:
	if(terceiro[2] >= quarto[2]):
		if(segundo[2] + quarto[1] >= terceiro[2] + primeiro[1]):
			print 2
		else:
			print 3
	else:
		if(segundo[2] + terceiro[1] >= quarto[2] + primeiro[1]):
			print 2
		else:
			print 4