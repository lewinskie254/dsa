def fibonacci(nthNumber):
    a, b = 1, 1
    for _ in range(1, nthNumber):
        a, b = b, a + b #get the next number in the fibonacci sequence 
    return a 

def fibonacciRecursive(nthNumber):
    if nthNumber == 1 or nthNumber == 2:
        #Base Case 
        return 1  
    else: 
        #Recursive Case 
        result = fibonacciRecursive(nthNumber - 1) + fibonacciRecursive(nthNumber - 2)
        return result 

print(fibonacciRecursive(10))