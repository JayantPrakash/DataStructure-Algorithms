from collections import deque

class Graph:

    def createAdjacencyList(self, n, edges):
        adjList = [[] for _ in range(n)]
        for (src, dst) in edges:
            adjList[src].append(dst)
            adjList[dst].append(src)
        return adjList

    def bfs(self, source, adjList):
        n = len(adjList)
        visited = [-1] * n
        queue = deque()
        queue.append(source)
        visited[source] = 1

        while len(queue) != 0:
            node = queue.popleft()
            print(node)
            #visited[node] = 1
            for neighbor in adjList[node]:
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
