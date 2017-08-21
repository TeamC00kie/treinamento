import math

linha = input().split(' ')
a, b, c = linha
a = float(a)
b = float(b)
c = float(c)

delta = pow(b, 2) - 4*a*c

if a != 0 and delta > 0:
	r1 = (-b + math.sqrt(delta)) / (2 * a)
	r2 = (-b - math.sqrt(delta)) / (2 * a)

	print('R1 = %.5f' % r1)
	print('R2 = %.5f' % r2)
else:
	print('Impossivel calcular')