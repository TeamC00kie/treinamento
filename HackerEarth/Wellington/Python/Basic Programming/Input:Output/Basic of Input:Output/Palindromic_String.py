s = raw_input()
reverse = s[::-1] #inverve string

if s == reverse:
	print('YES')
elif s != reverse:
	print('NO')