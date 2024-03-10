def exponentWithPowerRule(a, n):
    #Step 1: Determine the operations to be performed 
    opStack = []

    while n > 1: 
        if n % 2 == 0:
            #N is even 
            opStack.append('square')
            n = n // 2 
        elif n % 2 == 1:
            #N is odd 
            n -= 1 
            opStack.append('multiply')
    
    #Step 2: Perform iterations in reverse order 
    result = a #Start with the result as A
    
    print(opStack)
    while opStack:
        op = opStack.pop()
        print(opStack, op)
        if op == 'multiply':
            result *= a 
        if op == 'square':
            result *= result 
    
    #Return the Result 
    return result 

print(exponentWithPowerRule(3, 6))