# -*- coding: utf-8 -*-

linha = raw_input().split(' ')

horaInicio, minutoInicio, horaFim, minutoFim = linha
horaInicio = int(horaInicio)
horaFim = int(horaFim)
minutoInicio = int(minutoInicio)
minutoFim = int(minutoFim)

hora = horaFim - horaInicio
minuto = minutoFim - minutoInicio

if hora <= 0: #condições
	hora += 24
if minuto < 0:
	hora -= 1
	minuto += 60

print("O JOGO DUROU %i HORA(S) E %i MINUTO(S)" % (hora, minuto))