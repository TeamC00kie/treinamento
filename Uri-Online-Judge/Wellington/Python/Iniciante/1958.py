# -*- coding: utf-8 -*-

aux = raw_input()
numero = float(aux)

saida = "%.4e" % numero  # saida vai receber uma string com formato de notação cientifica
saida = saida.replace("e", "E")  # Trocar o e minusculo por maiusculo

aux = list(aux)
if numero == 0 and aux[0] != "-":
	print("+" + saida)
elif numero > 0:
	print("+" + saida)
else:
	print(saida)
