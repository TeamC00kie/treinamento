linha = input().split(' ')

a, b, c = linha

a = float(a)
b = float(b)
c = float(c)

triangulo = (a * c) /2;
print('TRIANGULO: %.3f' % triangulo)

circulo = 3.14159 * pow(c, 2)
print('CIRCULO: %.3f' % circulo)

trapezio = (c * (a + b))/2
print('TRAPEZIO: %.3f' % trapezio)

quadrado = pow(b, 2)
print('QUADRADO: %.3f' % quadrado)

retangulo = a * b
print('RETANGULO: %.3f' % retangulo)