#Find n'th fibonacci Number ------- with O(Log n)
#Alghorithm Design 1401 
MAX = 1000
f = [0] * MAX
def fib(n) : 
    # Base cases 
    if (n == 0) : 
        return 0
    if (n == 1 or n == 2) : 
        f[n] = 1
        return (f[n]) 
    if (f[n]) : 
        return f[n] 
    if( n & 1) : 
        k = (n + 1) // 2
    else :  
        k = n // 2
    if((n & 1) ) : 
        f[n] = (fib(k) * fib(k) + fib(k-1) * fib(k-1)) 
    else : 
        f[n] = (2*fib(k-1) + fib(k))*fib(k) 
    return f[n] 
#For_Example
n = 9
print(fib(n)) 
#output must be 34
  