tedad = int(input())
dict1={}
for index in range(0,tedad):
    motarjem = input()
    motarjem= motarjem.split(" ")
    dict1[motarjem[0]] = motarjem[1]

jomle = input()
jomle = jomle.split(' ')
jomle_jadid = []

for motarjem in jomle:
    jomle_jadid.append(dict1.get(motarjem,motarjem))           #get(keyname , value)
print(' '.join(jomle_jadid))
