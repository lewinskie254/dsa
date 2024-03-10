def hello(i=0):
    print(i, 'Hello World')
    i += 1

    if i < 5:
        hello(i)
    else: 
        return #Base Case 

hello()