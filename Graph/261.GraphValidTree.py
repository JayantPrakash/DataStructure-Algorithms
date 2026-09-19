# Key idea: Track the current node, the chosen subtree, and the value returned upward.
import collections
# Group the state and operations used by the GraphValidTree implementation.
class Solution:
    # Compute or update the valid tree result for the supplied input.
    def validTree(self,n,edges):
        adj_list = [ [] for _ in range(n)]

        # Process each value from `edges`.
        for (src,dist) in edges:
            adj_list[src].append(dist)
            adj_list[dist].append(src)

        visited = [-1] * n
        parent = [-1] * n

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
                        parent[neighbor] = node
                        q.append(neighbor)
                        visited[neighbor] = 1
                    else:
                        #condition for cross edge
                        if parent[node]!= neighbor:
                            return True
            return False

        num_components = 0

        # Process each value from `range(n)`.
        for v in range(n):
            # Choose this path when `visited[v] == -1` is true.
            if visited[v] == -1:
                num_components += 1
                # Choose this path when `num_components > 1` is true.
                if num_components > 1:
                    return False
                # Choose this path when `bfs(v)` is true.
                if bfs(v):
                    return False
        return True

n = 5
edges = [[0,1],[0,2],[0,3],[1,4]]
source = 0
g = Solution()
print(g.validTree(n,edges))

"""
For tree to be valid, it should have one component and there is no cross edge
T(n) = max(O(n),O(m))
S(n) = O(n)
"""