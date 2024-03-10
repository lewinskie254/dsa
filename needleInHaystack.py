#Iterative Function 
def findString(needle, haystack): 
    i = 0 
    while i < len(haystack):
        if haystack[i: i +len(needle)] == needle:
            return i #Needle Found 
        i += 1

#Recursive Function 
def findStringRecursive(needle, haystack, i=0):
    if i >= len(haystack):
        return -1 #Base Case: Needle not Found 
    if haystack[i:i+len(needle)] == needle:
        return i #Base Case: Needle Found 
    else: 
        #Recursive Case 
        return findStringRecursive(needle, haystack, i+1)

print(findStringRecursive('boozer', 'hayahaya haat haya haas boozer'))
print(2**64)