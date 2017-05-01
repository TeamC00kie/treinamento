# -*- coding: utf-8 -*-

a = map(int, raw_input().split())

feliz = False

if a[0] <= a[1]:
	feliz = True
else:
	feliz = False
if feliz and a[1] - a[0] > a[2] - a[1]:
	feliz = False
elif feliz and a[1] - a[0] < a[2] - a[1]:
	if a[1] == a[0] and a[1] > a[2]:
		feliz = False
	else:
		feliz = True
elif not feliz and a[0] - a[1] > a[1] - a[2]:
	feliz = True
elif not feliz and a[0] - a[1] < a[1] - a[2]:
	feliz = False
if a[0] == a[1] and a[1] == a[2]:
	feliz = False

if feliz:
	print(":)")
else:
	print(":(")