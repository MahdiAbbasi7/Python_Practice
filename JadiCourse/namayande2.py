max = -1
while True:
    n = int(input())
    if n>max :
        max2=max
        max = n
    elif n >max :
        max2 =n
    if n == -1:
        break
print (max2," ",max)