def ackermann(m, n, indentation=None):
    if indentation is None: 
        indentation = 0 
    print('%sackermann(%s,%s)' %(' ' * indentation, m, n))

    if m == 0:
        #Base Case 
        return n + 1
    elif m > 0 and n == 0:
        #Recursive Case 
        return ackermann(m-1, 1, indentation + 1)
    elif m > 0 and n > 0:
        #Recursive Case 
        return ackermann(m-1, ackermann(m, n -1, indentation + 1), indentation + 1)

print(ackermann(2, 2))