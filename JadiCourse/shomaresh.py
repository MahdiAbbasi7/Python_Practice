numofvalue=int(input())
thisdict={}
thislist=[]
for i in range(0,numofvalue):
    thislist.append(input())
#mohem
for char in thislist: 
    if char in thisdict.keys():
       thisdict[char] = thisdict[char]+1
    else:
        thisdict[char]=1 
#mohem
aval =list(thisdict.keys())
aval =sorted(aval)
for x in aval:
    print(x,"  ",thisdict[x])
