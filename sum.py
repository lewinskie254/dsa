#Iterative Function 
def sumIteration(n):
    total_sum = 0
    for i in range(n): 
        total_sum += (i+1)
    return total_sum

#Recursive Function 
def sumRecursion(n): 
    if n == 1:
        #Base Case 
        return 1 
    else: 
        #Recursive Case
        return sumRecursion(n-1) + n

print(sumRecursion(10))