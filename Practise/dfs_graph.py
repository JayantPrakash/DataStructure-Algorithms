class Graph:
    def createAdjacencyList(self, n, edges):
        adj_list = [[] for _ in range(n)]
        for src, dist in edges:
            adj_list[src].append(dist)
            adj_list[dist].append(src)
        return adj_list

    def dfs_helper(self, n, edges, source):
        self.adj_list = self.createAdjacencyList(n, edges)
        self.visited = [-1] * n 
        self.dfs(source)

    def dfs(self, u):
        self.visited[u] = 1
        print(u)
        for neighbor in self.adj_list[u]:
            if self.visited[neighbor] == -1:
                self.dfs(neighbor)      


n = 5
edges = [[0, 2], [0, 1], [2, 3], [3, 4]]
# edges = [[0, 1], [1, 2], [0, 2], [3, 4]]
source = 0
g = Graph()
g.dfs_helper(n, edges, 0)    