# Key idea: Trace the sorted edges and union-find decisions that build the spanning tree.
# Class to represent a graph
class Graph:

    # Initialize the state needed by a new instance.
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

    # Driver code
    def find(self, i):
        # Choose this path when `self.parent[i] == i` is true.
        if self.parent[i] == i:
            return i
        result = self.find(self.parent[i])
        self.parent[i] = result
        return result

    # Compute or update the kruskal mst result for the supplied input.
    def KruskalMST(self):
        self.graph = sorted(self.graph,
                            key=lambda item: item[2])

        # Process each value from `self.graph`.
        for u, v, w in self.graph:
            lu = self.find(u)
            lv = self.find(v)

            # cycle detected, not including in mst
            if lu == lv: continue

            # Choose this path when `lu != lv` is true.
            if lu != lv:
                # Choose this path when `self.size[lu] >= self.size[lv]` is true.
                if self.size[lu] >= self.size[lv]:
                    self.parent[lv] = lu
                    self.size[lu] += self.size[lv]
                else:
                    self.parent[lu] = lv
                    self.size[lv] += self.size[lu]

                self.components -= 1
                self.cost += w
                self.mst.append((u, v))
            # Choose this path when `self.components == 1` is true.
            if self.components == 1:
                return self.cost, self.mst

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
