# Key idea: Trace the queue one breadth-first level at a time.
from collections import defaultdict
from collections import deque

# Group the state and operations used by the bfs implementation.
class Graph:
    # Initialize the state needed by a new instance.
    def __init__(self):
        self.graph = defaultdict(list)

    # Record an edge in the graph representation.
    def addEdge(self,u,v):
        self.graph[u].append(v)

    # Traverse the reachable structure using BFS.
    def bfs(self,source):
        captured = {}
        visited = {}
        captured[source] = 1
        queue = deque()
        queue.append(source)

        # Keep processing while `len(queue) != 0` remains true.
        while len(queue)!= 0:
            u = queue.popleft()
            print(u)
            visited[u] = True
            captured[u] = True
            # Process each value from `self.graph[u]`.
            for v in self.graph[u]:
                # Choose this path when `v not in visited` is true.
                if v not in visited:
                    visited[v] = True
                    queue.append(v)


    # Compute or update the print vert result for the supplied input.
    def print_vert(self):
        #print(self.graph.keys())
        vert = []
        # Process each value from `self.graph.items()`.
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
g2.bfs('A')

