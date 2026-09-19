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

    # Driver code
    def find(self, i):
        if self.parent[i] == i:
            return i
        result = self.find(self.parent[i])
        self.parent[i] = result
        return result

    def KruskalMST(self):
        self.graph = sorted(self.graph,
                            key=lambda item: item[2])

        for u, v, w in self.graph:
            lu = self.find(u)
            lv = self.find(v)

            # cycle detected, not including in mst
            if lu == lv: continue

            if lu != lv:
                if self.size[lu] >= self.size[lv]:
                    self.parent[lv] = lu
                    self.size[lu] += self.size[lv]
                else:
                    self.parent[lu] = lv
                    self.size[lv] += self.size[lu]

                self.components -= 1
                self.cost += w
                self.mst.append((u, v))
            if self.components == 1:
                return self.cost, self.mst

        return -1


if __name__ == '__main__':
    g = Graph(4)
    g.addEdge(0, 1, 10)
    g.addEdge(0, 2, 6)
    g.addEdge(0, 3, 5)
    g.addEdge(1, 3, 15)
    g.addEdge(2, 3, 4)

    # Function call
    print(g.KruskalMST())
