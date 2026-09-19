# Count DFS starts across all vertices: one complete traversal marks one undirected component.
# O(V + E) time and storage, including adjacency lists; recursion may reach depth V.
def number_of_connected_components(n, edges):
    """
    Args:
     n(int32)
     edges(list_list_int32)
    Returns:
     int32
    """
    adjList = [[] for _ in range(n)]
    for (src, dst) in edges:
        adjList[src].append(dst)
        adjList[dst].append(src)
    visited = [-1] * n

    # Mark before exploring neighbors so the reverse edge and other cycles cannot recurse forever.
    def dfs(u):
        visited[u] = 1
        # print(u)
        for neighbour in adjList[u]:
            if visited[neighbour] == -1:
                dfs(neighbour)

    component = 0
    for v in range(n):
        # Every still-unseen vertex begins a different component, even when it has no edges.
        if visited[v] == -1:
            component += 1
            dfs(v)
    return component