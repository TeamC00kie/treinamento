# -*- coding: utf-8 -*-

bi = {'---': 0, '--*': 1, '-*-': 2, '-**': 3, '*--': 4, '*-*': 5, '**-': 6, '***': 7}
numeros = []
for i in range(3):
    soma = 0
    while True:
        entrada = raw_input()
        if entrada == "caw caw":
            break
        soma += bi[entrada]

    numeros.append(soma)

for x in numeros:
    print x