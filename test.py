x = [0, 1]
count = 0

if len(x) == 1: 
    if x[0] == 0: 
        count = 1
else: 
    for i in range(len(x)-1):
        if x[i] == 0 and x[i+1] == 1: 
            count += 1

print(count)
