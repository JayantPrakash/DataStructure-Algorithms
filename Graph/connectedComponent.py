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
    for (src, dst) in edges:
        adjList[src].append(dst)
        adjList[dst].append(src)
    visited = [-1] * n

    def dfs(u):
        visited[u] = 1
        # print(u)
        for neighbour in adjList[u]:
            if visited[neighbour] == -1:
                dfs(neighbour)

    component = 0
    for v in range(n):
        if visited[v] == -1:
            component += 1
            dfs(v)
    return component