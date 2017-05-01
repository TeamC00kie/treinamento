# -*- coding: utf-8 -*-

linha = raw_input().split(' ')
diaInicio = int(linha[1])
linha = raw_input().split(' : ')
horaInicio, minutoInicio, segundoInicio = linha
horaInicio = int(horaInicio)
minutoInicio = int(minutoInicio)
segundoInicio = int(segundoInicio)

linha = raw_input().split(' ')
diaFim = int(linha[1])
linha = raw_input().replace(' ', '').split(':')
horaFim, minutoFim, segundoFim = linha
horaFim = int(horaFim)
minutoFim = int(minutoFim)
segundoFim = int(segundoFim)

dia = diaFim - diaInicio
hora = horaFim - horaInicio
minuto = minutoFim - minutoInicio
segundo = segundoFim - segundoInicio

if segundo < 0:
	segundo += 60
	minuto -= 1
if minuto < 0:
	minuto += 60
	hora -= 1
if hora < 0:
	hora += 24
	dia -= 1

print("%i dia(s)" % dia)
print("%i hora(s)" % hora)
print("%i minuto(s)" % minuto)
print("%i segundo(s)" % segundo)