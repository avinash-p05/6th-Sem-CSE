from collections import defaultdict

graph = defaultdict(list)


def addEdge(u, v):
    graph[u].append(v)


def dfs(start, goal, depth):
    print(start, end=" ")
    if start == goal:
        return True
    if depth <= 0:
        return False
    for i in graph[start]:
        if dfs(i, goal, depth - 1):
            return True
    return False


def dfid(start, goal, maxDepth):
    print("Start Node : ", start, " Goal Node : ", goal)
    for i in range(maxDepth):
        print("DFID at level ", i + 1)
        print("Path taken : ", end=" ")
        pathFound = dfs(start, goal, i)
        if pathFound:
            print("\n Goal Node Found!!")
            return
        else:
            print("\n Goal Node not Found!!")


addEdge("A", "B")
addEdge("A", "C")
addEdge("A", "D")
addEdge("B", "E")
addEdge("B", "F")
addEdge("D", "G")
addEdge("D", "H")
addEdge("G", "K")
addEdge("G", "L")

dfid("A", "L", 4)
