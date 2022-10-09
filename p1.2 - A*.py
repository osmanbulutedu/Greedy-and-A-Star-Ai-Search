# HW2 - P1-2 A* Search  (Osman Bulut-001530539)

import queue as Q

graph = {
    'a': {'b': 2, 'c': 2},
    'b': {'a': 2, 'd': 1},
    'c': {'a': 2, 'd': 8, 'f': 3},
    'd': {'b': 1, 'c': 8, 'e': 2, 'S': 3},
    'e': {'d': 2, 'h': 8, 'r': 2, 'S': 9},
    'f': {'c': 3, 'G': 2, 'r': 2},
    'G': {'f': 2},
    'h': {'e': 8, 'p': 4, 'q': 4},
    'p': {'h': 4, 'q': 15, 'S': 1},
    'q': {'h': 4, 'p': 15},
    'r': {'e': 2, 'f': 2},
    'S': {'d': 3, 'e': 9, 'p': 1}
}

h_scores = {'S': 10, 'a': 5, 'b': 7, 'c': 4, 'd': 7, 'e': 5, 'f': 2, 'G': 0, 'h': 11, 'p': 14, 'q': 12, 'r': 3}


def astar(graph, source, destination):
    visited = []
    path = ['G']
    parents = {source: 'None'}
    queue = Q.PriorityQueue()
    queue.put((10, source))
    h2 = 0

    while queue:
        cost, node = queue.get()

        if node not in visited:
            visited.append(node)

            if node == destination:
                if destination in parents:
                    i = destination
                    while not path[-1] == source:
                        path.append(parents[i])
                        i = path[-1]

                return visited, list(reversed(path))

            children = graph[node]
            for i in children:
                if i not in visited:
                    total_cost = cost + children[i]
                    h1 = h_scores[i]
                    total = total_cost + h1 - h_scores[node]
                    queue.put((total, i))
                    parents[i] = node


solution, path = (astar(graph, 'S', 'G'))

print("The expanded vertex list---->", solution)
print("The return path is ---->",path)

