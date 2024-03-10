def rev(theString):
    if len(theString) == 0 or len(theString) == 1:
        #Base Case 
        return theString
    else: 
        #Recursive Case 
        head = theString[0]
        tail = theString[1:]
        return rev(tail) + head 

print(rev('sugar pop'))