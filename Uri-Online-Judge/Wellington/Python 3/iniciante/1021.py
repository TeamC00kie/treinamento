n = float(input())
notas = int(n)
moedas = int((n-notas)*100)

print('NOTAS:')
print(int(notas/100) ,'nota(s) de R$ 100.00')
notas %= 100
print(int(notas/50) ,'nota(s) de R$ 50.00')
notas %= 50
print(int(notas/20) ,'nota(s) de R$ 20.00')
notas %= 20
print(int(notas/10) ,'nota(s) de R$ 10.00')
notas %= 10
print(int(notas/5) ,'nota(s) de R$ 5.00')
notas %= 5
print(int(notas/2) ,'nota(s) de R$ 2.00')
notas %= 2

print('MOEDAS:')
#Apesar do 1 ser uma moeda ele ainda é um número inteiro
print(int(notas) ,'moeda(s) de R$ 1.00')
print(int(moedas/50) ,'moeda(s) de R$ 0.50')
moedas %= 50
print(int(moedas/25) ,'moeda(s) de R$ 0.25')
moedas %= 25
print(int(moedas/10) ,'moeda(s) de R$ 0.10')
moedas %= 10
print(int(moedas/5) ,'moeda(s) de R$ 0.05')
moedas %= 5
print(int(moedas) ,'moeda(s) de R$ 0.01')