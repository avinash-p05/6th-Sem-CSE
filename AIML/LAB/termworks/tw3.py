import heapq

def a_star(graph,start,goal):
    openList = [(0,start)]
    parents = {}
    g_v = {node:float('inf') for node in graph}
    g_v[start]=0

    f_v = {node: float('inf') for node in graph}
    f_v[start] = graph[start][1]

    it=0

    while openList:
        current_f,current_node = heapq.heappop(openList)
        if current_node==goal:
            path=[]
            while current_node in parents:
                path.append(current_node)
                current_node = parents[current_node]
            path.append(start)
            final_cost = g_v[goal]
            print("The Final cost is ",final_cost)
            return path[::-1]

        for child,cost in graph[current_node][0].items():
            t_g = g_v[current_node]+cost
            if t_g <g_v[child]:
                parents[child]= current_node
                g_v[child]=t_g
                f_v[child]= t_g+graph[child][1]
                heapq.heappush(openList,(f_v[child],child))

        it+=1
        print(f"Iteration : {it}")
        print("The Current path : ")
