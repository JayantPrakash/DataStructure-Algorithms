from heapq import heappush, heappop


class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]
        self.captured = [-1] * vertices
        self.components = vertices
        self.cost = 0
        self.mst = []
        # Function to add an edge to graph

    def addEdge(self, u, v, w):
        self.graph[u].append([w, v])
        self.graph[v].append([w, u])

    def prims(self):
        pq = []
        self.captured[0] = 1
        for cost, node in self.graph[0]:
            heappush(pq, (cost, (0, node)))

        while len(pq) != 0:
            cost, (parent, node) = heappop(pq)
            if self.captured[node] == 1:
                continue
            self.cost += cost
            self.mst.append([parent, node])
            self.captured[node] = 1

            for cost, neighbor in self.graph[node]:
                if self.captured[neighbor] == -1:
                    heappush(pq, (cost, (node, neighbor)))

        return self.cost, self.mst


if __name__ == '__main__':
    g = Graph(4)
    g.addEdge(0, 1, 10)
    g.addEdge(0, 2, 6)
    g.addEdge(0, 3, 5)
    g.addEdge(1, 3, 15)
    g.addEdge(2, 3, 4)

    # Function call
    print(g.prims())
