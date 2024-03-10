def factorial(number):
    product = 1
    for i in range(1, number+1):
        product = product * i
    return product 


def factorialRecursion(number):
    if number == 1:
        return 1 
    return factorial(number - 1) * number

print(factorialRecursion(5))