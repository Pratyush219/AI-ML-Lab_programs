def getDist(node, g):
    return g[node] + heuristic(node)

def printPath(path):
    print('Path found:')
    print(path)
def aStar(graph, start, end):
    openSet = set(start)
    closedSet = set()
    g = dict()
    g[start] = 0
    parent = dict()
    parent[start] = None
    while len(openSet) > 0:
        n = None
        for node in openSet:
            if n == None or getDist(node, g) < getDist(n, g):
                n = node
        if n == end:
            path = []
            node = n
            while node != None:
                path.append(node)
                node = parent[node]
            path.reverse()
            return path
        elif getNeighbors(graph, n) != None:
            for node, wt in getNeighbors(graph, n):
                if node not in openSet and node not in closedSet:
                    g[node] = g[n] + wt
                    parent[node] = n
                    openSet.add(node)
                else:
                    if g[n] + wt < g[node]:
                        g[node] = g[n] + wt
                        parent[node] = n
                        if node in closedSet:
                            closedSet.remove(node)
                            openSet.add(node)
        openSet.remove(n)
        closedSet.add(n)
    print('Path not found')
    return None

def getNeighbors(graph, node):
    if node not in graph:
        return None
    return graph[node]
def heuristic(node):
    H = {
        'A': 14,
        'B': 8,
        'C': 10,
        'D': 7,
        'E': 9,
        'F': 999,
        'G': 0
    }
    if node in H:
        return H[node]
    return None
graph = {
    'A': [('B', 3), ('C', 2)],
    'B': [('D', 5), ('E', 4)],
    'C': [('F', 7)],
    'D': [('G', 6)],
    'E': [('G', 2)]
}
path = aStar(graph, 'A', 'G')
print(path)