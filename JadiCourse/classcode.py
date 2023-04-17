n = ""

for i in range(1, 5001):
    n += str(i)

k = int(input(""))

count = 1
for digit in n:
    if count == k:
        print(digit)
    count += 1