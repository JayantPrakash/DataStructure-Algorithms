# Key idea: Trace the recursive or explicit-stack depth-first traversal and its return values.
# Group the state and operations used by the dfs graph implementation.
class Graph:
    # Compute or update the create adjacency list result for the supplied input.
    def createAdjacencyList(self, n, edges):
        adj_list = [[] for _ in range(n)]
        # Process each value from `edges`.
        for src, dist in edges:
            adj_list[src].append(dist)
            adj_list[dist].append(src)
        return adj_list

    # Compute or update the dfs helper result for the supplied input.
    def dfs_helper(self, n, edges, source):
        self.adj_list = self.createAdjacencyList(n, edges)
        self.visited = [-1] * n 
        self.dfs(source)

    # Traverse the reachable structure using DFS.
    def dfs(self, u):
        self.visited[u] = 1
        print(u)
        # Process each value from `self.adj_list[u]`.
        for neighbor in self.adj_list[u]:
            # Choose this path when `self.visited[neighbor] == -1` is true.
            if self.visited[neighbor] == -1:
                self.dfs(neighbor)      


n = 5
edges = [[0, 2], [0, 1], [2, 3], [3, 4]]
# edges = [[0, 1], [1, 2], [0, 2], [3, 4]]
source = 0
g = Graph()
g.dfs_helper(n, edges, 0)    