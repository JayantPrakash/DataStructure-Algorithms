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

    # Grow a minimum spanning tree from vertex 0 using the cheapest frontier edge.
    # Heap entries hold (edge weight, (parent, destination)); weights are not path distances.
    def prims(self):
        pq = []
        self.captured[0] = 1
        for cost, node in self.graph[0]:
            heappush(pq, (cost, (0, node)))

        while len(pq) != 0:
            cost, (parent, node) = heappop(pq)
            # Skip edges whose destination entered the tree via an earlier, cheaper candidate.
            if self.captured[node] == 1:
                continue
            self.cost += cost
            # Accept exactly one incoming edge for each newly captured vertex.
            self.mst.append([parent, node])
            self.captured[node] = 1

            for cost, neighbor in self.graph[node]:
                if self.captured[neighbor] == -1:
                    # Add candidate cut edges from the new vertex to uncaptured neighbors.
                    heappush(pq, (cost, (node, neighbor)))

        # Returns only the component containing 0 on disconnected input, and state persists across calls.
        # The lazy edge heap takes O(E log(E + 1)) time and O(V + E) space.
        return self.cost, self.mst


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
