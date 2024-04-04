from collections import deque

def bfs(grapgh,start):
    visited = set()
    queue = deque([start])
    while queue:
        node =queue.popleft()
        if node not in visited:
            print(node , end=" ")
            visited.add(node)
            queue.extend(grapgh[node])

grapgh ={
    "A":['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':[],
    'F':[]
}
bfs(grapgh,'A')