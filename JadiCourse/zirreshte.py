vorodi = input()
a = vorodi.replace("AB","@")
b = vorodi.replace("BA","#")

if ('@' in a) or ('#' in b):
    print("YES")
else:
    print("NO")
