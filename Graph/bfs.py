from collections import defaultdict
from collections import deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    # This stores a directed edge u -> v; no reverse edge is inserted.
    def addEdge(self,u,v):
        self.graph[u].append(v)

    # Use a FIFO frontier to visit reachable vertices in breadth-first order.
    # The visited dictionary prevents repeated work; expected O(V + E) time and O(V) traversal space.
    def bfs(self,source):
        captured = {}
        visited = {}
        captured[source] = 1
        queue = deque()
        queue.append(source)

        while len(queue)!= 0:
            # Process the oldest discovered vertex before vertices discovered from it.
            u = queue.popleft()
            print(u)
            visited[u] = True
            captured[u] = True
            for v in self.graph[u]:
                # Mark neighbors on enqueue so multiple incoming edges cannot schedule the same vertex twice.
                if v not in visited:
                    visited[v] = True
                    queue.append(v)


    # Display the adjacency mapping: each source followed by its outgoing neighbors.
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
g2.bfs('A')

