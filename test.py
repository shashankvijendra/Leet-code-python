def farthest_nodes(strArr):
    # Create an adjacency list representation of the graph
    graph = {}
    for path in strArr:
        a, b = path.split('-')
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)

    # Initialize arrays for levels, distances, and endpoints
    n = len(graph)
    lvl = [0] * n
    dist1 = [-1] * n
    dist2 = [-1] * n
    end1, end2, maxi = 0, 0, 0

    # DFS to find the first endpoint
    def find_first_end(u, p):
        nonlocal maxi, end1
        lvl[u] = 1 + lvl[p]
        if lvl[u] > maxi:
            maxi = lvl[u]
            end1 = u
        for v in graph[u]:
            if v != p:
                find_first_end(v, u)

    # Clear arrays and find the second endpoint
    def clear(n):
        for i in range(n):
            lvl[i] = 0
        maxi = 0
        dist1[0] = dist2[0] = -1

    # DFS to find the second endpoint
    def find_second_end(u, p):
        nonlocal maxi, end2
        lvl[u] = 1 + lvl[p]
        if lvl[u] > maxi:
            maxi = lvl[u]
            end2 = u
        for v in graph[u]:
            if v != p:
                find_second_end(v, u)

    # DFS to find distances from the first endpoint
    def find_distance_from_first(u, p):
        dist1[u] = 1 + dist1[p]
        for v in graph[u]:
            if v != p:
                find_distance_from_first(v, u)

    # DFS to find distances from the second endpoint
    def find_distance_from_second(u, p):
        dist2[u] = 1 + dist2[p]
        for v in graph[u]:
            if v != p:
                find_distance_from_second(v, u)

    # Find the endpoints and distances
    find_first_end(0, 0)
    clear(n)
    find_second_end(end1, 0)
    find_distance_from_first(end1, 0)
    find_distance_from_second(end2, 0)

    # Determine the farthest node for each node
    result = []
    for i in range(n):
        x, y = dist1[i], dist2[i]
        result.append(end1 if x >= y else end2)

    return result

# Example usage
input_strArr = ["a-b", "b-c", "b-d"]
print(farthest_nodes(input_strArr))  # Output: [1, 1, 1, 1, 2, 2, 2]
