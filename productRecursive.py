numbers = [1, 2, 3, 4, 5, 6, 7, 19, 23, 15, 17]

def product(numbers):
    if len(numbers) == 1:
        return numbers[0]
    elif len(numbers) > 1: 
        index_number = numbers.pop()
        return index_number * product(numbers)

print(product(numbers))