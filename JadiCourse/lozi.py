n = int(input(""))

space = " "
star = "*"

row = n // 2
for i in range(-row, row + 1):
    print((space * (abs(i)) + star * ((row - abs(i)) *2 + 1) + space * (abs(i))) * 2)