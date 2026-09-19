from heapq import heappush,heappop
class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [ [] for _ in range(vertices)]
        self.captured = [-1] * vertices
        self.distance = [-1] * vertices
        # Function to add an edge to graph

    def addEdge(self, u, v, w):
        self.graph[u].append([w, v])
        self.graph[v].append([w, u])

    # With nonnegative weights, the cheapest queued path to an uncaptured node finalizes its distance.
    # This lazy heap may hold O(E) candidate paths; typical time is O((V + E) log(E + 1)).
    def dijkstra(self, source):
        pq = []
        # This implementation hard-codes vertex 0 as captured, so its initialization assumes source == 0.
        # Captured/distance arrays persist on the instance; repeated independent runs do not reset them.
        self.captured[0] = 1
        for cost, node,  in self.graph[source]:
            heappush(pq,(cost,(source,node)))
        self.distance[source] = 0
        while len(pq) != 0:
            cost, (parent,node) = heappop(pq)
            # Discard a stale path when another cheaper candidate already finalized this vertex.
            if self.captured[node] == 1:
                continue
            # The heap key is the full source-to-node path cost, not just the last edge weight.
            self.distance[node]= cost
            self.captured[node] = 1

            for cost, neighbor in self.graph[node]:
                if self.captured[neighbor] == -1:
                    # Extend the finalized path by one edge; unreachable vertices retain distance -1.
                    heappush(pq,(cost + self.distance[node],(node,neighbor)))

        return self.distance

# Run this example only when the file is executed directly.
if __name__ == '__main__':
    g = Graph(4)
    g.addEdge(0, 1, 10)
    g.addEdge(0, 2, 6)
    g.addEdge(0, 3, 5)
    g.addEdge(1, 3, 15)
    g.addEdge(2, 3, 4)

    # Function call
    source = 0
    print(g.dijkstra(source))
