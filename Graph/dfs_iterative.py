from collections import defaultdict
from collections import deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    # Store a directed edge; callers must add the reverse direction if they want an undirected graph.
    def addEdge(self,u,v):
        self.graph[u].append(v)

    # Replace recursion with a LIFO stack: the last discovered neighbor is processed next.
    # Expected O(V + E) time and O(V) frontier/visited space.
    def dfs(self,source):
        captured = {}
        visited = {}
        captured[source] = 1
        stack = deque()
        stack.append(source)

        while len(stack)!= 0:
            # Pop from the same end used for insertion to obtain depth-first rather than breadth-first order.
            u = stack.pop()
            print(u)
            visited[u] = True
            captured[u] = True
            for v in self.graph[u]:
                # Mark when pushing to avoid duplicate stack entries through converging graph paths.
                if v not in visited:
                    visited[v] = True
                    stack.append(v)


    # Print each source vertex and its outgoing neighbors.
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

