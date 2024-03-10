def sumPowerOf2(n):
    a = 0
    for i in range(n): 
        a += 2**(i+1) 
    return a 

print(sumPowerOf2(100))

def sumPowerRecursive(n): 
    if n == 1:
        #Base Case 
        return 2
    else: 
        #Recursive Case 
        return sumPowerRecursive(n-1) + 2**n

print(sumPowerRecursive(100))