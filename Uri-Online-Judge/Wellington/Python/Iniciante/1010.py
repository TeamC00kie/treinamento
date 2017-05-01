linha = raw_input().split(' ') #ler linha e quebra nos ' '
c1, q1, v1 = linha #atribui linha[0] = c1 e assim por diante
c1 = int(c1) #converte valores para inteiros
q1 = int(q1)
v1 = float(v1)

linha = raw_input().split(' ')
c2, q2, v2 = linha
c2 = int(c2)
q2 = int(q2)
v2 = float(v2)

total = (q1 * v1) + (q2 * v2) #multiplica quantidade pelo valor e soma

print("VALOR A PAGAR: R$ %.2f" % total) #imprimi total com duas casas decimais