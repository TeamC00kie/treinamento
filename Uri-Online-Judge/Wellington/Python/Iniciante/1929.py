# -*- coding: utf-8 -*-

t = map(int, raw_input().split())
t.sort()

if abs(t[0]-t[1]) < t[2] and t[2] < t[0] + t[1] or abs(t[0] - t[2]) < t[1] and t[1] < t[0] + t[2] or abs(t[1]+t[2]) < t[0] and t[0] < t[1] + t[2]:
	print("S")
elif abs(t[3]-t[1]) < t[2] and t[2] < t[3] + t[1] or abs(t[3] - t[2]) < t[1] and t[1] < t[3] + t[2] or abs(t[1]+t[2]) < t[3] and t[3] < t[1] + t[2]:
	print("S")
else:
	print("N")