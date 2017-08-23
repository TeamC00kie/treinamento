# -*- coding: utf-8 -*-

linha = list(map(int, input().split()))
horaInicio, minutoInicio, horaFim, minutoFim = linha

if (horaInicio >= horaFim):
	hora = (horaFim + 24) - horaInicio
else:
	hora = horaFim - horaInicio
if (minutoInicio > minutoFim):
	minuto = (minutoFim + 60) - minutoInicio
	hora -= 1
else:
	minuto = minutoFim - minutoInicio

print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(hora, minuto))