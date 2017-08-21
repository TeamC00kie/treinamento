linha = input().split(' ')
codigo, quantidade = linha
codigo = int(codigo)
quantidade = int(quantidade)

if codigo == 1:
	print('Total: R$ %.2f' % (quantidade * 4))
elif codigo == 2:
	print('Total: R$ %.2f' % (quantidade * 4.5))
elif codigo == 3:
	print('Total: R$ %.2f' % (quantidade * 5))
elif codigo == 4:
	print('Total: R$ %.2f' % (quantidade * 2))
elif codigo == 5:
	print('Total: R$ %.2f' % (quantidade * 1.5))