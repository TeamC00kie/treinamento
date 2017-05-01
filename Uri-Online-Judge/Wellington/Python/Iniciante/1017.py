# -*- coding: utf-8 -*-

carro = 12.0 #km por litro

horas = input() #ler valores
velocidade = input()

distancia = horas * velocidade #calculo distancia

combustivel = distancia / carro #combustivel gasto na viagem

print("%.3f" % combustivel) #imprimir combustivel com 3 casas decimais