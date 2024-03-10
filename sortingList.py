new_list = [1, 4, 5, 6, 7, 8, 12, 34, 10]


for i in range(len(new_list)):
    for j in range(len(new_list)-1):
        if new_list[j] > new_list[j+1]:
            tmp = new_list[j]
            new_list[j] = new_list[j+1]
            new_list[j+1] = tmp 


print(new_list)