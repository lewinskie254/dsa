call_stack = []
call_stack.append({'return address': 'start', 'number': 5})
return_value = None 

while len(call_stack) > 0:
    number = call_stack[-1]['number']
    return_address = call_stack[-1]['return address']

    if return_address == 'start':
        if number == 1:
            #Base Case
            return_value = 1
            break 
        else: 
            call_stack[-1]['return address'] == 'after recursive call'
            call_stack.append({'return address': 'start', 'number': number - 1})
            continue 
    elif return_address == 'after recursive call':
        return_value = number * return_value
        break 

    print(return_value)

print(call_stack)