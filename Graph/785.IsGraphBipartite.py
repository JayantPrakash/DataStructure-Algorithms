# Key idea: Track visited or connected state as vertices and edges are processed.
import collections
# Group the state and operations used by the IsGraphBipartite implementation.
class Solution:
    # Compute or update the is bipartite result for the supplied input.
    def isBipartite(self,graph):
        n = len(graph)
        adj_list = graph

        visited = [-1] * n
        parent = [-1] * n
        distance = [-1] * n
        # Traverse the reachable structure using BFS.
        def bfs(source):
            q = collections.deque()
            q.append(source)
            visited[source] = 1
            distance[source] = 0
            dist = 0
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
                        distance[neighbor] = distance[node] + 1
                    else:
                        #condition for cross edge
                        if parent[node] != neighbor:
                            #condition to check if node and neighbour is on same level
                            #if it is on same level, its odd length cycle
                            #otherwise its even length cycle
                            if distance[neighbor] == distance[node]:
                                return False
            return True

        #num_components = 0

        for v in range(n):
            # Choose this path when `visited[v] == -1` is true.
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