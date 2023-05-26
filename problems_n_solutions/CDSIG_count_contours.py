def solution(adj):
    n = len(adj)
    graph = {i: set() for i in range(n)}

    for i in range(n):
        for j in range(n):
            if adj[i][j] == True:
                graph[i].add(j)

    stars = 0
    visited = set()
    all_candis = []

    for i in range(n):
        if (graph[i]) and (i not in visited):
            candidates = set()
            visited, candidates = dfs(graph=graph, node=i, visited=visited, candidates=candidates)
            if candidates not in all_candis:
                all_candis += [list(candidates)]

    for candi in all_candis:
        if len(candi) == 2:
            stars += 1
        else:
            adj_list = [len(graph[i]) for i in candi]
            rest = [i for i in adj_list if i != max(adj_list)]

            if max(adj_list) + 1 == len(candi) and \
                    list(set(rest)) == [1]: stars += 1

    return stars


def dfs(graph, node, visited, candidates=set()):
    if node not in visited:
        visited.add(node)
        candidates.add(node)
        if graph[node] and visited != set(graph.keys()):
            for nd in graph[node]:
                if nd not in visited and node != nd:
                    visited, candidates = dfs(
                        graph=graph,
                        node=nd,
                        visited=visited,
                        candidates=candidates)
    return visited, candidates