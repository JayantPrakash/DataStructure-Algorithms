# Key idea: Trace the recursive or explicit-stack depth-first traversal and its return values.
from collections import defaultdict


# Group the state and operations used by the dfs implementation.
class Graph:
    # Initialize the state needed by a new instance.
    def __init__(self):
        self.graph = defaultdict(list)

    # Record an edge in the graph representation.
    def addEdge(self,u,v):
        self.graph[u].append(v)


    # Compute or update the explore result for the supplied input.
    def explore(self,v, visited):
        visited.append(v)
        print('visited::',visited,'\n')
        print('\n',v,end = '')

        # Process each value from `self.graph[v]`.
        for neighbour in self.graph[v]:
            # Choose this path when `neighbour not in visited` is true.
            if neighbour not in visited:
                self.explore(neighbour, visited)

    # Traverse the reachable structure using DFS.
    def DFS(self, v):
        visited = []

        #print('keys::',self.graph.keys())
        #for vertex in self.graph.keys():
        if v not in visited:
            self.explore(v,visited)
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

print("Following is DFS from (starting from vertex 2)")
g.DFS('A')
