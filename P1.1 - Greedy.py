# HW2 - P1-1 Greedy Search  (Osman Bulut-001530539)
from queue import PriorityQueue

graph = {
    'a': {'b': 2, 'c': 2},
    'b': {'a': 2, 'd': 1},
    'c': {'a': 2, 'd': 8, 'f': 3},
    'd': {'b': 1, 'c': 8, 'e': 2, 's': 3},
    'e': {'d': 2, 'h': 8, 'r': 2, 's': 9},
    'f': {'c': 3, 'g': 2, 'r': 2},
    'g': {'f': 2},
    'h': {'e': 8, 'p': 4, 'q': 4},
    'p': {'h': 4, 'q': 15, 's': 1},
    'q': {'h': 4, 'p': 15},
    'r': {'e': 2, 'f': 2},
    's': {'d': 3, 'e': 9, 'p': 1}
}

heuristic = {'s': 10, 'a': 5, 'b': 7, 'c': 4, 'd': 7, 'e': 5, 'f': 2, 'g': 0, 'h': 11, 'p': 14, 'q': 12, 'r': 3}


def greedysearch(graph, source, destination):
    expanded = []  # Our initial parameters
    q = PriorityQueue()
    q.put((10, source))
    visited = set()

    while q:

        weight, vertex = q.get()  # we save our current weight of the edge(cost) and vertex
        last = vertex[-1]  # we need to check the last member of our corresponding branch.That's why we used vertex[-1].
        if last not in visited:
            visited.add(last)
            expanded.append(last) # if not, we will add it into both our set and list. Bcs we need them distinctively.

            if last == destination: #if reach the destionation, the loop should break
                return vertex, expanded

            children = graph[last]  # if not, we will determine children of our vertex.

            for i in children: #visited check for each child
                if i not in visited:
                    q.put((heuristic[i], vertex + i)) #we put the vertex heuristic cost and and vertex into our queue


solution, expanded = greedysearch(graph, 's', 'g')
print('The return path is ----> ', solution)
print("The expanded vertex list until reaching the destination is ---->", expanded)






