from collections import defaultdict
from collections import deque


class Graph():
    #def __int__(self, n):
    #    self.visited = [-1] * n

    def createAdjacencyList(self, n, edges):
        adjList = [[] for _ in range(n)]
        for (src, dst) in edges:
            adjList[src].append(dst)
            adjList[dst].append(src)
        return adjList

    def dfs_helper(self,n,edges, source):
        self.adjList = self.createAdjacencyList(n,edges)
        self.visited = [-1] * n
        self.dfs(source)

    def dfs(self, u):
        n = len(self.adjList)
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

