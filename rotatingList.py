sorted_list = [1, 4, 5, 6, 7, 8, 10, 12, 34, 45]
new_list = []
count = 0
last_item = sorted_list[-1]

iteration = 1

for i in range(len(sorted_list)):
    new_list = sorted_list[-count:] + sorted_list[:-count] 
    print(count, new_list, last_item)
    count += 1

for j in range(len(new_list)):
    if new_list[j] == last_item:
        print(iteration)
        break
    else: 
        iteration += 1

