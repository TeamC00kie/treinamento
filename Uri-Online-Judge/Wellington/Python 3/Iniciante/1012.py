# -*- coding: utf-8 -*-

linha = list(map(float, input().split()))

a, b, c = linha

triangulo = (a * c) / 2
print('TRIANGULO: {:.3f}'.format(triangulo))

circulo = 3.14159 * c ** 2
print('CIRCULO: {:.3f}'.format(circulo))

trapezio = (c * (a + b))/2
print('TRAPEZIO: {:.3f}'.format(trapezio))

quadrado = pow(b, 2)
print('QUADRADO: {:.3f}'.format(quadrado))

retangulo = a * b
print('RETANGULO: {:.3f}'.format(retangulo))