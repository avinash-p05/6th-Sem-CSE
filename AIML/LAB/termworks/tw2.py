
tree= {
    'S':[[('A', 7), ('B', 8)], 15],
    'A': [[('C', 4), ('D', 7)], 12],
    'B': [[('E', 2), ('F', 5)], 8],
    'C': [[('I', 12)], 10],
    'D': [[('J', 15)], 11],
    'E': [[('G',3), ('H', 7)], 6],
    'F': [[('K',3)], 7],
    'G':[[],0],
    'H':[[],12]
}

start = 'S'
goal = 'G'



def bsf():
    queue=[(start,0,tree[start][1])]
    path = []

    while True:
        queue = get_sorted(queue)
        node, path_cost,_ = queue.pop(0)
        path.append(node)
        if node == goal:
            return True,path,path_cost
        childrens = get_children(node)

        for child, cost in childrens:
            queue.append((child,path_cost+cost,tree[child][1]))

    return False,[],0

def get_children(node):
    return tree[node][0]

def get_sorted(queue):
    return sorted(queue,key=lambda x: x[2])

success, path_taken ,total_cost = bsf()

if success:
    print("Goal node reached!")
    print("Total Cost : ",total_cost)
    print("Path Taken : ",path_taken)

else:
    print("Goal node unreachable!!")