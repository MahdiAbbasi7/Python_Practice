def divisor(num) :
    for i in range(num) :
         x = len([i for i in range(1,num+1) if not num % i])
    return x

nums=[]
for i in range(1,21):
    pre_num = int(input(""))
    if (pre_num > 0):
        nums.append([divisor(pre_num),pre_num])
    else :
        print("non zero or smaller number!")

nums.sort()
print(nums[len(nums)-1])
