says = input()
status = "no"
if('h' in says) and ('e'in says)and ('ll'in says)and ('o'in says):
    status = 'yes'
else:
    status = "no"
h = says.find("h") #1
e = says.find("e") #2
ll = says.find("ll") #3 & 4
o= says.find("o") #5
if status == "yes" and o>ll and ll > e and e > h :
    print("yes")
else:
    print("no")

#helhcludoo ro no mide vali bayad yes bede
