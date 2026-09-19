# Key idea: Trace the frontier heap as the minimum spanning tree grows.
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
# Group the state and operations used by the Prims implementation.
class Graph:

    # Initialize the state needed by a new instance.
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

    # Compute or update the prims result for the supplied input.
    def prims(self):
        pq = []
        self.captured[0] = 1

        # Process each value from `self.graph[0]`.
        for node,cost in self.graph[0]:
            heappush(pq,(cost,(0,node)))

        # Keep processing while `len(pq) != 0` remains true.
        while len(pq) != 0:
            min_neighbor = heappop(pq)
            # Choose this path when `self.captured[min_neighbor[1][1]] == 1` is true.
            if self.captured[min_neighbor[1][1]] == 1:
                continue
            self.cost += min_neighbor[0]
            self.mst.append(min_neighbor)
            self.captured[min_neighbor[1][1]] = 1

            # Process each value from `self.graph[min_neighbor[1][1]]`.
            for node, cost in self.graph[min_neighbor[1][1]]:
                # Choose this path when `self.captured[node] == -1` is true.
                if self.captured[node] == -1:
                    heappush(pq,(cost,(min_neighbor[1][1],node)))

        return self.mst,self.cost

# Run this example only when the file is executed directly.
if __name__ == '__main__':
    g = Graph(4)
    g.addEdge(0, 1, 10)
    g.addEdge(0, 2, 6)
    g.addEdge(0, 3, 5)
    g.addEdge(1, 3, 15)
    g.addEdge(2, 3, 4)

    # Function call
    print(g.prims())





