from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    # Store a directed edge; traversal follows only explicitly recorded directions.
    def addEdge(self,u,v):
        self.graph[u].append(v)


    # Mark before recursive descent to break cycles and retain the visitation order.
    def explore(self,v, visited):
        visited.append(v)
        print('visited::',visited,'\n')
        print('\n',v,end = '')

        for neighbour in self.graph[v]:
            # visited is a list here: each membership check is O(V), unlike a set-based DFS.
            # Across E examined edges this can take O(VE) time, with O(V) visited/stack space.
            if neighbour not in visited:
                self.explore(neighbour, visited)

    # Start fresh traversal state for the requested vertex; disconnected regions are not explored.
    def DFS(self, v):
        visited = []

        #print('keys::',self.graph.keys())
        #for vertex in self.graph.keys():
        if v not in visited:
            self.explore(v,visited)
    # Print the adjacency mapping to inspect which outgoing edges traversal can follow.
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

print("Following is DFS from (starting from vertex 2)")
g.DFS('A')
