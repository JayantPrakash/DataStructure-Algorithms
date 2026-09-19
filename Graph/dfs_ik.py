from collections import defaultdict
from collections import deque


class Graph():
    #def __int__(self, n):
    #    self.visited = [-1] * n

    # Represent an undirected graph by recording each edge in both adjacency lists.
    def createAdjacencyList(self, n, edges):
        adjList = [[] for _ in range(n)]
        for (src, dst) in edges:
            adjList[src].append(dst)
            adjList[dst].append(src)
        return adjList

    # Reset traversal state for this call; only the source's connected component will be visited.
    def dfs_helper(self,n,edges, source):
        self.adjList = self.createAdjacencyList(n,edges)
        self.visited = [-1] * n
        self.dfs(source)

    # Recursion explores one neighbor's entire reachable branch before resuming the next neighbor.
    # Visited checks give O(V + E) time; the recursion stack can grow to O(V).
    def dfs(self, u):
        n = len(self.adjList)
        # Mark before descending so cycles cannot lead back into an active or completed vertex.
        self.visited[u] = 1
        print(u)
        for neighbour in self.adjList[u]:
            if self.visited[neighbour] == -1:
                self.dfs(neighbour)


n = 5
edges = [[0, 2], [0, 1], [2, 3], [3, 4]]
# edges = [[0, 1], [1, 2], [0, 2], [3, 4]]
source = 0
g = Graph()
g.dfs_helper(n, edges, 0)

