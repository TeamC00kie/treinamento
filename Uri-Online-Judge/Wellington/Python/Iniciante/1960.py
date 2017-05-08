# -*- coding: utf-8 -*-
import sys

n = raw_input()
tamanho = len(n)

if tamanho == 3:
	if n[0] == '1':
		print("C"),
		sys.stdout.write("")
	elif n[0] == '2':
		print("CC"),
		sys.stdout.write("")
	elif n[0] == '3':
		print("CCC"),
		sys.stdout.write("")
	elif n[0] == '4':
		print("CD"),
		sys.stdout.write("")
	elif n[0] == '5':
		print("D"),
		sys.stdout.write("")
	elif n[0] == '6':
		print("DC"),
		sys.stdout.write("")
	elif n[0] == '7':
		print("DCC"),
		sys.stdout.write("")
	elif n[0] == '8':
		print("DCCC"),
		sys.stdout.write("")
	elif n[0] == '9':
		print("CM"),
		sys.stdout.write("")
if tamanho == 3 or tamanho == 2:
	b = tamanho - 2  #para saber a posição do vetor que deve ser lida na comparação 
	if n[b] == '1':
		print("X"),
		sys.stdout.write("")
	elif n[b] == '2':
		print("XX"),
		sys.stdout.write("")
	elif n[b] == '3':
		print("XXX"),
		sys.stdout.write("")
	elif n[b] == '4':
		print("XL"),
		sys.stdout.write("")
	elif n[b] == '5':
		print("L"),
		sys.stdout.write("")
	elif n[b] == '6':
		print("LX"),
		sys.stdout.write("")
	elif n[b] == '7':
		print("LXX"),
		sys.stdout.write("")
	elif n[b] == '8':
		print("LXXX"),
		sys.stdout.write("")
	elif n[b] == '9':
		print("XC"),
		sys.stdout.write("")

b = tamanho - 1
if n[b] == '1':
	print("I"),
	sys.stdout.write("")
elif n[b] == '2':
	print("II"),
	sys.stdout.write("")
elif n[b] == '3':
	print("III"),
	sys.stdout.write("")
elif n[b] == '4':
	print("IV"),
	sys.stdout.write("")
elif n[b] == '5':
	print("V"),
	sys.stdout.write("")
elif n[b] == '6':
	print("VI"),
	sys.stdout.write("")
elif n[b] == '7':
	print("VII"),
	sys.stdout.write("")
elif n[b] == '8':
	print("VIII"),
	sys.stdout.write("")
elif n[b] == '9':
	print("IX"),
	sys.stdout.write("")

print("")