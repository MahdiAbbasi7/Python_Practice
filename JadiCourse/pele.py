n = int(input(""))

def ways(steps):
    if steps == 0:
        return 1
    elif steps < 0:
        return 0
    else:
        return ways(steps - 5) + ways(steps - 2) + ways(steps - 1)

totalways = ways(n)
print(totalways)