from queue import PriorityQueue

graph = {
    "A": [(146, "O"), (140, "S"), (494, "C")],
    "O": [(146, "A"), (151, "S")],
    "S": [(151, "O"), (140, "A"), (80, "R"), (99, "F")],
    "C": [(494, "A"), (146, "R")],
    "R": [(80, "S"), (146, "C"), (97, "P")],
    "F": [(99, "S"), (211, "B")],
    "B": [(211, "F"), (101, "P")],
    "P": [(101, "B"), (97, "R"), (138, "C")]
}

def ucs(graph, start, goal):
    visited = set()
    queue = PriorityQueue()
    queue.put((0, start))
    cost_so_far = {start: 0}
    prev = {}

    while not queue.empty():
        cost, node = queue.get()
        if node == goal:
            path = []
            while node != start:
                path.append(node)
                node = prev[node]
            path.append(start)
            path.reverse()
            return cost, path

        if node not in visited:
            visited.add(node)
            for neighbor_cost, neighbor in graph[node]:
                new_cost = cost + int(neighbor_cost)
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    prev[neighbor] = node
                    queue.put((new_cost, neighbor))

    return float('inf'), None

start_node = "A"
goal_node = "B"
cost, path = ucs(graph, start_node, goal_node)
print("UCS traversal:", path)
print("Cost:", cost)
