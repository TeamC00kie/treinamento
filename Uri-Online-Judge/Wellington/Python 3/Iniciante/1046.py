# -*- coding: utf-8 -*-

linha = list(map(int, input().split()))
horaInicio, horaFim = linha

if (horaInicio >= horaFim):
	horas = (horaFim + 24) - horaInicio
else:
	horas = horaFim - horaInicio

print('O JOGO DUROU {} HORA(S)'.format(horas))