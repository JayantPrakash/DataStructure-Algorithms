# Key idea: Track visited or connected state as vertices and edges are processed.
# Compute or update the number of connected components result for the supplied input.
def number_of_connected_components(n, edges):
    """
    Args:
     n(int32)
     edges(list_list_int32)
    Returns:
     int32
    """
    # Write your code here.
    adjList = [[] for _ in range(n)]
    # Process each value from `edges`.
    for (src, dst) in edges:
        adjList[src].append(dst)
        adjList[dst].append(src)
    visited = [-1] * n

    # Traverse the reachable structure using DFS.
    def dfs(u):
        visited[u] = 1
        # print(u)
        for neighbour in adjList[u]:
            # Choose this path when `visited[neighbour] == -1` is true.
            if visited[neighbour] == -1:
                dfs(neighbour)

    component = 0
    # Process each value from `range(n)`.
    for v in range(n):
        # Choose this path when `visited[v] == -1` is true.
        if visited[v] == -1:
            component += 1
            dfs(v)
    return component