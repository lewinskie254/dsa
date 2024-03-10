#exponents by iteration 
def exponentByIteration(a, n):
    result = 1 
    for _ in range(n):
        result *= a
    return result

#Exponents by Recursion 
def exponentsByRecursion(a, n):
    if n == 1:
        return a 
    elif n % 2 == 0:
        #Recursive Case 
        result = exponentsByRecursion(a, n // 2)
        print("result", result)
        return result * result 
    elif n % 2 == 1:
        result = exponentsByRecursion(a, n // 2)
        print("result", result)
        return result * result * a 
        

print(exponentsByRecursion(10, 3))