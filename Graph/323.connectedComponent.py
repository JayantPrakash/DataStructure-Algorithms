# Key idea: Track visited or connected state as vertices and edges are processed.
import collections
# Group the state and operations used by the connectedComponent implementation.
class Solution:
    # Compute or update the count components result for the supplied input.
    def countComponents(self,n,edges):
        adj_list = [ [] for _ in range(n)]

        # Process each value from `edges`.
        for (src,dist) in edges:
            adj_list[src].append(dist)
            adj_list[dist].append(src)

        visited = [-1] * n
        # Traverse the reachable structure using BFS.
        def bfs(source):
            q = collections.deque()
            q.append(source)
            visited[source] = 1

            # Keep processing while `len(q) != 0` remains true.
            while len(q) != 0:
                node = q.popleft()
                visited[node] = 1
                # Process each value from `adj_list[node]`.
                for neighbor in adj_list[node]:
                    # Choose this path when `visited[neighbor] == -1` is true.
                    if visited[neighbor] == -1:
                        q.append(neighbor)
                        visited[neighbor] = 1

        num_components = 0

        # Process each value from `range(n)`.
        for v in range(n):
            # Choose this path when `visited[v] == -1` is true.
            if visited[v] == -1:
                bfs(v)
                num_components += 1

        return num_components

n = 5
edges = [[0, 1], [1, 2], [0, 2]
         #,[2, 3]
    , [3, 4]]
source = 0
g = Solution()
print(g.countComponents(n,edges))

