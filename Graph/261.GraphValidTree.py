import collections
class Solution:
    # An undirected tree must be connected and have no cycle; BFS checks both conditions.
    # Adjacency construction and traversal take O(V + E) time and O(V + E) storage.
    def validTree(self,n,edges):
        adj_list = [ [] for _ in range(n)]

        for (src,dist) in edges:
            # Store both directions because an undirected edge is reachable from either endpoint.
            adj_list[src].append(dist)
            adj_list[dist].append(src)

        visited = [-1] * n
        parent = [-1] * n

        # Return True when a cycle is found, not when traversal succeeds.
        def bfs(source):
            q = collections.deque()
            q.append(source)
            visited[source] = 1

            while len(q) != 0:
                node = q.popleft()
                visited[node] = 1

                for neighbor in adj_list[node]:
                    if visited[neighbor] == -1:
                        # Mark on discovery so two frontier vertices cannot enqueue the same unseen vertex.
                        parent[neighbor] = node
                        q.append(neighbor)
                        visited[neighbor] = 1
                    else:
                        # The edge back to the parent is expected; any other already-discovered neighbor closes a cycle.
                        if parent[node]!= neighbor:
                            return True
            return False

        num_components = 0

        for v in range(n):
            if visited[v] == -1:
                num_components += 1
                # A new traversal after the first component proves the graph is disconnected.
                if num_components > 1:
                    return False
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