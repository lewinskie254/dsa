def sums(numbers):
    if len(numbers) == 0: 
        #Base Case 
        return 0
    else: 
        #Recursive Case
        head = numbers[0]
        tail = numbers[1:]
        return head + sums(tail)

nums = [5, 2, 4, 8]
print(sums(nums))
