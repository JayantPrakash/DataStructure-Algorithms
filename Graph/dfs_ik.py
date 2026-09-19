# Key idea: Trace the recursive or explicit-stack depth-first traversal and its return values.
from collections import defaultdict
from collections import deque


# Group the state and operations used by the dfs ik implementation.
class Graph():
    #def __int__(self, n):
    #    self.visited = [-1] * n

    def createAdjacencyList(self, n, edges):
        adjList = [[] for _ in range(n)]
        # Process each value from `edges`.
        for (src, dst) in edges:
            adjList[src].append(dst)
            adjList[dst].append(src)
        return adjList

    # Compute or update the dfs helper result for the supplied input.
    def dfs_helper(self,n,edges, source):
        self.adjList = self.createAdjacencyList(n,edges)
        self.visited = [-1] * n
        self.dfs(source)

    # Traverse the reachable structure using DFS.
    def dfs(self, u):
        n = len(self.adjList)
        self.visited[u] = 1
        print(u)
        # Process each value from `self.adjList[u]`.
        for neighbour in self.adjList[u]:
            # Choose this path when `self.visited[neighbour] == -1` is true.
            if self.visited[neighbour] == -1:
                self.dfs(neighbour)


n = 5
edges = [[0, 2], [0, 1], [2, 3], [3, 4]]
# edges = [[0, 1], [1, 2], [0, 2], [3, 4]]
source = 0
g = Graph()
g.dfs_helper(n, edges, 0)

