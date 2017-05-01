nome = raw_input() #ler valores
salario = input()
vendas = input()

comissao = vendas * 0.15 #15% das vendas
salarioTotal = comissao + salario #soma salario com comissao

print("TOTAL = R$ %.2f" % salarioTotal) #imprimi salario final