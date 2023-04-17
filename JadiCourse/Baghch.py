n , m = input().split(' ')
n = int(n)
m = int(m)
x = []
for i in range(m):
    x.append(input())
for i in range(n):
    count = 0
    for j in range(m):
        if  (x[j][i] == 'W'):
            count += 1
    if (count%2 == 0):
        print('B',end='')
    else:
        print('F',end='')
        