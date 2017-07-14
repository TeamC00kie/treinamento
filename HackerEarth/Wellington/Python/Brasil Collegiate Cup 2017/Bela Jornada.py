n = input()
c = map(int, raw_input().split())

meio = 0
if n % 2 == 0:
	meio = n/2 + 1
else:
	meio = n/2 + 1

s1 = 0
s2 = 0

for x in range(n):
	if x >= meio:
		s2 += c[x]
	else:
		s1 += c[x]
s = s1 * s2

print(s)