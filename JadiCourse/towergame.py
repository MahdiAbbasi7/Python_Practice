def hanoi(n, source, target, helper):   #source = first   helper = second   target = third
    if n > 0:
        hanoi(n-1, source, helper, target)

        target.append(source.pop())
        print(first, second, third, sep="\n")

        print(sep="\n")

        hanoi(n-1, helper, target, source)
    
n = int(input())
first = []
for i in range(n):
    first.append(i+1)
second = []
third = []

print(first, second, third, sep="\n")
print(sep="\n")

hanoi(n, first, third, second)
print(2**n -1)