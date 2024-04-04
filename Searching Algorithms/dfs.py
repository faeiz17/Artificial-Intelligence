def dfs(grapgh , start):
    visited = set()
    stack = [start]
    while stack:
        node=stack.pop()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            stack.extend(reversed(grapgh[node]))

grapgh ={
    "A":['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':[],
    'F':[]
}
dfs(grapgh,'A')