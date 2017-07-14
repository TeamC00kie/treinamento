#Uri não está aceitando
# -*- coding: utf-8 -*-

n = input()
estrela = []
for x in range(n):
    estrela.append(0)

i = 0
carneiros = map(int, raw_input().split())

while(True):
    if i == 0 and carneiros[i] % 2 == 0:
        estrela[i] = 1
        if carneiros[i] > 0:
            carneiros[i] -= 1
        break
    elif i == n - 1 and carneiros[i] % 2 == 1:
        estrela[i] = 1
        if carneiros[i] > 0:
            carneiros[i] -= 1
        break
    elif carneiros[i] % 2 == 1:
        carneiros[i] -= 1
        estrela[i] = 1
        i += 1
    elif carneiros[i] % 2 == 0:
        estrela[i] = 1
        if carneiros[i] > 0:
            carneiros[i] -= 1
        i -= 1

print("%i %i" % (sum(estrela), sum(carneiros)))