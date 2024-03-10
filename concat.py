name_list = ["hello", "world"]

def strings(name_list):

    new_name = ''.join(name_list)
    
    if len(new_name) == 1: 
        #Base Case 
        return new_name
    else:
        head = new_name[:1]
        tail = new_name[1:]
        return head + strings(tail)

print(strings(name_list))


