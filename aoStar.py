class Graph:
    def __init__(self, graph, heuristic, start):
        self.graph = graph
        self.heuristic = heuristic
        self.start = start
        self.solved = set()
        self.parent = dict()
        self.solution = dict()
        self.parent[self.start] = self.start
    def applyAoStar(self):
        self.aoStar(self.start, False)
    def printSolution(self):
        print('For solution graph, traverse from the start node')
        print('Solution:', self.solution)
    def getMinCostNodes(self, node):
        if node not in self.graph:
            return 0, []
        minCost = float('inf')
        nodes = []
        for childArc in self.graph[node]:
            cur_nodes = []
            cost = 0
            for childNode, wt in childArc:
                cost += self.heuristic[childNode] + wt
                cur_nodes.append(childNode)
            if cost < minCost:
                minCost = cost
                nodes = cur_nodes
        return minCost, nodes
    def aoStar(self, node, backtracking):
        print('Heuristic values:', self.heuristic)
        print('Solution graph:', self.solution)
        print('Processing node:', node)
        print('-----------------------------------------------------------------------------------------------')

        if node not in self.solved:
            minCost, childNodes = self.getMinCostNodes(node)
            print(minCost, childNodes)
            nodeSolved = True
            self.heuristic[node] = minCost
            for child in childNodes:
                self.parent[child] = node
                if child not in self.solved:
                    nodeSolved = False
            if nodeSolved:
                self.solved.add(node)
                self.solution[node] = childNodes
            if node != self.start:
                self.aoStar(self.parent[node], True)
            if not backtracking:
                for child in childNodes:
                    if child in self.solved:
                        self.solved.remove(child)
                    self.aoStar(child, False)

h = {'A': 1, 'B': 6, 'C': 12, 'D': 10, 'E': 4, 'F': 4, 'G': 5, 'H': 7}
graph = {
    'A': [[('B', 1), ('C', 1)], [('D', 1)]],
    'B': [[('G, 1')], [('H', 1)]],
    'D': [[('E', 1), ('F', 1)]]
}
h1 = {'A': 1, 'B': 6, 'C': 2, 'D': 12, 'E': 2, 'F': 1, 'G': 5, 'H': 7, 'I': 7, 'J': 1}
graph1 = {
    'A': [[('B', 1), ('C', 1)], [('D', 1)]],
    'B': [[('G', 1), ('H', 1)]],
    'C': [[('J', 1)]],
    'D': [[('E', 1), ('F', 1)]],
    'G': [[('I', 1)]]
}
G1 = Graph(graph, h, 'A')
G1.applyAoStar()
G1.printSolution()