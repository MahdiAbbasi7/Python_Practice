x = input()
 
w = ""
for i in x:
    w = i + w
 
if (x == w):
    print("palindrome")
else:
    print("not palindrome")