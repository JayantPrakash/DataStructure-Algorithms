import collections
class Solution:
    def countComponents(self,n,edges):
        adj_list = [ [] for _ in range(n)]

        for (src,dist) in edges:
            adj_list[src].append(dist)
            adj_list[dist].append(src)

        visited = [-1] * n
        def bfs(source):
            q = collections.deque()
            q.append(source)
            visited[source] = 1

            while len(q) != 0:
                node = q.popleft()
                visited[node] = 1
                for neighbor in adj_list[node]:
                    if visited[neighbor] == -1:
                        q.append(neighbor)
                        visited[neighbor] = 1

        num_components = 0

        for v in range(n):
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

