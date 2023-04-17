from math import sqrt
n=int(input())
L=[]
for i in range(n):
	a=int(input())
	L.append(sqrt(a))
for i in L:
	print('%.4f' % i) #" .4f " for python