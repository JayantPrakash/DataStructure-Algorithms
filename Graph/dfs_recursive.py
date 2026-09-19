from collections import defaultdict
from collections import deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.visited = {}

    # Store only u -> v; this adjacency mapping describes a directed graph.
    def addEdge(self,u,v):
        self.graph[u].append(v)

    # Mark the current vertex, then fully explore each still-unseen outgoing branch.
    # Expected O(V + E) time and O(V) stack space; visited persists across calls on this instance.
    def dfs(self,u):
        #visited = {}
        self.visited[u] = True
        print(u)
        for v in self.graph[u]:
            # Skip active and completed vertices alike so directed cycles cannot recurse indefinitely.
            if v not in self.visited:
                self.dfs(v)

    # Display the stored outgoing adjacency lists.
    def print_vert(self):
        #print(self.graph.keys())
        vert = []
        for item in self.graph.items():
            print(item[0],item[1])

g = Graph()
g.addEdge('A', 'B')
g.addEdge('A', 'E')
g.addEdge('E', 'I')
g.addEdge('E', 'J')
g.addEdge('I', 'J')
#g.print_vert()
#g.bfs('A')
#print("Following is DFS from (starting from vertex 2)")
#g.DFS('A')

g2 = Graph()
g2.addEdge('A','B')
g2.addEdge('A','E')
g2.addEdge('B','C')
g2.addEdge('B','F')
g2.addEdge('C','D')
g2.addEdge('C','G')
g2.addEdge('D','C')
g2.addEdge('D','E')
g2.addEdge('D','G')
g2.addEdge('F','G')
g2.dfs('A')

