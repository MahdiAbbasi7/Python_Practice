price=[]
quality=[]
c=0
x=input()
for i in range(0,int(x)):
 y=input()
 price.append(y[:2])
 quality.append(y[2:])
for j in range(0,len(price)):
    for e in range(0,len(price)):
        if int(price[j])<int(price[e]) and int(quality[j])>int(quality[e]):
         c=c+1
if c>=1:
 print('happy irsa')
else:
 print('poor irsa') 