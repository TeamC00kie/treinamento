s = raw_input()
s = list(s) #Quebra string

for x in range(len(s)):
	if s[x].isupper():
		s[x] = s[x].lower()
	elif s[x].islower():
		s[x] = s[x].upper()
s = ''.join(s) #Junta string

print(s)