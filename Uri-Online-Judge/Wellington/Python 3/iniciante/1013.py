linha = input().split(' ')

a, b, c = linha
a = int(a)
b = int(b)
c = int(c)

maiorAB = int((a + b + abs(a-b))/2)
maior = int((maiorAB + c + abs(maiorAB - c))/2)

print(maior,'eh o maior')