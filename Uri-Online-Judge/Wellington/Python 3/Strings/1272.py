n = int(input())
frases = []

for x in range(n):
	frases.append(input())

for x in range(n):
	descrip = ''
	primeira = True
	for i in range(len(frases[x])):
		if frases[x][i] != ' ' and primeira:
			descrip +=  frases[x][i]
			primeira = False
		elif frases[x][i] == ' ' and not primeira:
			primeira = True
	print(descrip)