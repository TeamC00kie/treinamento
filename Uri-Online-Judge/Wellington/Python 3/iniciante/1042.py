numeros = input().split(' ')

ordenado = []

for aux in numeros:
	ordenado.append(int(aux))

ordenado.sort()
for aux in ordenado:
	print(aux)

print()

for aux in numeros:
	print(aux)