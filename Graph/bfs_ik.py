# Key idea: Trace the queue one breadth-first level at a time.
from collections import deque

# Group the state and operations used by the bfs ik implementation.
class Graph:

    # Compute or update the create adjacency list result for the supplied input.
    def createAdjacencyList(self, n, edges):
        adjList = [[] for _ in range(n)]
        # Process each value from `edges`.
        for (src, dst) in edges:
            adjList[src].append(dst)
            adjList[dst].append(src)
        return adjList

    # Traverse the reachable structure using BFS.
    def bfs(self, source, adjList):
        n = len(adjList)
        visited = [-1] * n
        queue = deque()
        queue.append(source)
        visited[source] = 1

        # Keep processing while `len(queue) != 0` remains true.
        while len(queue) != 0:
            node = queue.popleft()
            print(node)
            #visited[node] = 1
            for neighbor in adjList[node]:
                # Choose this path when `visited[neighbor] == -1` is true.
                if visited[neighbor] == -1:
                    visited[neighbor] = 1
                    queue.append(neighbor)


n = 5
edges = [[0, 1], [1, 2], [0, 2], [2,3],[3, 4]]
#edges = [[0, 1], [1, 2], [0, 2], [3, 4]]
source = 0
g = Graph()
adjList = g.createAdjacencyList(n, edges)
print(adjList)
g.bfs(source, adjList)
