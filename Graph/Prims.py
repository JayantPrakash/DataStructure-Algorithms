from heapq import heappush,heappop
"""
h = []
heappush(h, (0, ['u','v']))
heappush(h, (7, 'release product'))
heappush(h, (1, 'write spec'))
heappush(h, (3, 'create tests'))
print(h)
print(heappop(h)[1][0])
"""
class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [ [] for _ in range(vertices)]
        self.parent = list(range(vertices))
        self.captured = [-1] * vertices
        self.components = vertices
        self.cost = 0
        self.mst = []
        # Function to add an edge to graph

    def addEdge(self, u, v, w):
        self.graph[u].append([v, w])
        self.graph[v].append([u, w])

    def prims(self):
        pq = []
        self.captured[0] = 1

        for node,cost in self.graph[0]:
            heappush(pq,(cost,(0,node)))

        while len(pq) != 0:
            min_neighbor = heappop(pq)
            if self.captured[min_neighbor[1][1]] == 1:
                continue
            self.cost += min_neighbor[0]
            self.mst.append(min_neighbor)
            self.captured[min_neighbor[1][1]] = 1

            for node, cost in self.graph[min_neighbor[1][1]]:
                if self.captured[node] == -1:
                    heappush(pq,(cost,(min_neighbor[1][1],node)))

        return self.mst,self.cost

if __name__ == '__main__':
    g = Graph(4)
    g.addEdge(0, 1, 10)
    g.addEdge(0, 2, 6)
    g.addEdge(0, 3, 5)
    g.addEdge(1, 3, 15)
    g.addEdge(2, 3, 4)

    # Function call
    print(g.prims())





