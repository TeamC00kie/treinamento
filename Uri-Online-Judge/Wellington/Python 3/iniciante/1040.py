# -*- coding: utf-8 -*-

linha = input().split()
n1, n2, n3, n4 = linha
n1 = float(n1) * 2
n2 = float(n2) * 3
n3 = float(n3) * 4
n4 = float(n4)

media = (n1 + n2 + n3 + n4)/10

print('Media: %.1f' % media)
if media >= 7:
	print('Aluno aprovado.')
elif media < 5:
	print('Aluno reprovado.')
else:
	print('Aluno em exame.')
	nExame = float(input())
	print('Nota do exame: %.1f' % nExame)
	media = (media + nExame)/2
	if media >= 5:
		print('Aluno aprovado.')
	else:
		print('Aluno reprovado')
	print('Media final: %.1f' % media)