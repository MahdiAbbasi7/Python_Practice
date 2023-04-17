import random
from secrets import choice

hads = random.randint( 1,99)
print (hads)

javabe_man = input("which one mahdi ? k , b , d ?   ")
answer =hads
while javabe_man != 'd' :
    if javabe_man == 'b' :
        hads2= random.randrange(answer,99)
        
        print(hads2)
    elif javabe_man =='k':
        hads3 = random.randrange(1,answer ) 
        
        print (hads3)
    
print("wooooowwwwww")

#کرش کردن در دو ماژول کوچیکتر و بزرگتر 