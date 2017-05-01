linha = raw_input().split(' ') #ler valores na mesma linha e quebra em vetor

a, b, c = linha #atribui valores do vetor as variaveis

a = int(a) #transforma string em int
b = int(b)
c = int(c)

maiorAB = (a + b + abs(a - b))/2 #calculo para saber maior
maior = (maiorAB + c + abs(maiorAB - c))/2

print(str(maior) + " eh o maior") #imprimi maior valor