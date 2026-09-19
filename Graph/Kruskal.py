# Class to represent a graph
class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.parent = list(range(vertices))
        self.size = [1] * vertices
        self.components = vertices
        self.cost = 0
        self.mst = []
        # Function to add an edge to graph

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    # Follow parent links to the component leader and compress the path on the return journey.
    def find(self, i):
        if self.parent[i] == i:
            return i
        result = self.find(self.parent[i])
        self.parent[i] = result
        return result

    # Process edges from cheapest to most expensive; accept an edge only if it joins two components.
    # Sorting dominates at O(E log E); union-find uses path compression and union by size.
    def KruskalMST(self):
        self.graph = sorted(self.graph,
                            key=lambda item: item[2])

        for u, v, w in self.graph:
            lu = self.find(u)
            lv = self.find(v)

            # Equal leaders mean a path already connects the endpoints; adding this edge would create a cycle.
            if lu == lv: continue

            if lu != lv:
                # Attach the smaller component's root to the larger one to keep parent chains shallow.
                if self.size[lu] >= self.size[lv]:
                    self.parent[lv] = lu
                    self.size[lu] += self.size[lv]
                else:
                    self.parent[lu] = lv
                    self.size[lv] += self.size[lu]

                self.components -= 1
                self.cost += w
                self.mst.append((u, v))
            # One component means V-1 joining edges have connected the graph; the spanning tree is complete.
            if self.components == 1:
                return self.cost, self.mst

        # For the usual V >= 2 case, exhausting edges without connectivity means no spanning tree exists.
        # This version also returns -1 for a one-vertex graph and retains state between method calls.
        return -1


# Run this example only when the file is executed directly.
if __name__ == '__main__':
    g = Graph(4)
    g.addEdge(0, 1, 10)
    g.addEdge(0, 2, 6)
    g.addEdge(0, 3, 5)
    g.addEdge(1, 3, 15)
    g.addEdge(2, 3, 4)

    # Function call
    print(g.KruskalMST())
