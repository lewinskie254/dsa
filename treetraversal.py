root = {'data': 'A', 'Children': []}
node2 = {'data': 'B', 'Children': []}
node3 = {'data': 'C', 'Children': []}
node4 = {'data': 'D', 'Children': []}
node5 = {'data': 'E', 'Children': []}
node6 = {'data': 'F', 'Children': []}
node7 = {'data': 'G', 'Children': []}
node8 = {'data': 'H', 'Children': []}

root['Children'] = [node2, node3]
node2['Children'] = [node4]
node3['Children'] =[node5, node6]
node5['Children'] = [node7, node8]

def preOrderTraverse(node):
    print(node['data'], end=" ") #Access this Node's Data 
    if len(node['Children']) > 0:
        #Recursive Case 
        for child in node['Children']:
            preOrderTraverse(child) #Traverse the child nodes 
    #Base Case
    return 

def postOrderTraverse(node):
    for child in node['Children']:
        #Recursive Case 
        postOrderTraverse(child) #Traverse the child nodes 
    print(node['data'], end=" ") #Access this node's data 
    #Base Case 
    return 

def inOrderTraverse(node):
    if len(node['Children']) >= 1: 
        #Recursive Case 
        inOrderTraverse(node['Children'][0]) #Traverse the Left Child 
    print(node['data'], end=" ") #Access this node's data 
    if len(node['Children']) >= 2:
        #Recursive Case 
        inOrderTraverse(node['Children'][1]) #Traverse the Right Child
    #Base Case 
    return 

inOrderTraverse(root)
print()
postOrderTraverse(root)
print()
preOrderTraverse(root)