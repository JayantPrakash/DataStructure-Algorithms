import collections
class Solution:
    # An undirected graph is bipartite exactly when it has no odd cycle; acyclic graphs qualify too.
    # BFS depth parity supplies the two colors. Check every component in O(V + E) time.
    def isBipartite(self,graph):
        n = len(graph)
        adj_list = graph

        visited = [-1] * n
        parent = [-1] * n
        distance = [-1] * n
        def bfs(source):
            q = collections.deque()
            q.append(source)
            visited[source] = 1
            distance[source] = 0
            dist = 0
            while len(q) != 0:
                node = q.popleft()
                visited[node] = 1
                for neighbor in adj_list[node]:
                    if visited[neighbor] == -1:
                        parent[neighbor] = node
                        q.append(neighbor)
                        visited[neighbor] = 1
                        # A newly discovered neighbor is one level farther away and gets the opposite parity.
                        distance[neighbor] = distance[node] + 1
                    else:
                        if parent[node] != neighbor:
                            # In undirected BFS, edge endpoints differ by at most one level.
                            # An edge within one level joins equal colors and certifies an odd cycle.
                            if distance[neighbor] == distance[node]:
                                return False
            return True

        #num_components = 0

        # Disconnected components need separate BFS roots; one invalid component rejects the graph.
        for v in range(n):
            if visited[v] == -1:
                #num_components += 1
                #if num_components > 1:
                #    return False
                if bfs(v) is False:
                    return False
        return True

#n = 5
#edges = [[0,1],[0,2],[0,3],[1,4]]
graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
#graph = [[1,3],[0,2],[1,3],[0,2]]
#source = 0
g = Solution()
print(g.isBipartite(graph))

"""
For tree to be bipartite, it should have even length cycle.
Even legth cycle - cross edge not on the same level
Odd legth - cross edge on the same level 
T(n) = max(O(n),O(m))
S(n) = O(n)
"""