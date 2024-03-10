def ispalindrome(theString):
    if len(theString) == 0 or len(theString) == 1:
        #Base Case 
        return True 
    else: 
        #Recursive Case 
        head =theString[0]
        middle= theString[1:-1]
        last =theString[-1]
        return head == last and ispalindrome(middle) 

print(ispalindrome("tacocat"))