class Graph:
    # Represent an undirected graph by storing each edge at both endpoints.
    def createAdjacencyList(self, n, edges):
        adj_list = [[] for _ in range(n)]
        for src, dist in edges:
            adj_list[src].append(dist)
            adj_list[dist].append(src)
        return adj_list

    # Initialize fresh adjacency/visited state, then explore only the component reachable from source.
    def dfs_helper(self, n, edges, source):
        self.adj_list = self.createAdjacencyList(n, edges)
        self.visited = [-1] * n 
        self.dfs(source)

    # Mark on entry, recursively finish each unseen neighbor's branch, then return to the caller.
    # O(V + E) time and up to O(V) recursion depth.
    def dfs(self, u):
        self.visited[u] = 1
        print(u)
        for neighbor in self.adj_list[u]:
            # A visited neighbor may be the parent or part of another cycle; skip it to avoid repeated recursion.
            if self.visited[neighbor] == -1:
                self.dfs(neighbor)      


n = 5
edges = [[0, 2], [0, 1], [2, 3], [3, 4]]
# edges = [[0, 1], [1, 2], [0, 2], [3, 4]]
source = 0
g = Graph()
g.dfs_helper(n, edges, 0)    