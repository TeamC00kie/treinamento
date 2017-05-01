linha = raw_input().split(' ') #ler valores e quebra em um vetor

a, b, c = linha #atribui valores do vetor as variaveis

a = float(a) #converte para float
b = float(b)
c = float(c)

triangulo = (a * c) /2; #calculos
circulo = 3.14159 * (c ** 2)
trapezio = (c * (a + b))/2
quadrado = (b ** 2)
retangulo = a * b

print("TRIANGULO: %.3f" % triangulo) #imprimi resultados com 3 casas decimais
print("CIRCULO: %.3f" % circulo)
print("TRAPEZIO: %.3f" % trapezio)
print("QUADRADO: %.3f" % quadrado)
print("RETANGULO: %.3f" % retangulo)