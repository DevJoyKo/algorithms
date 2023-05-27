def solution(adj):
    n = len(adj)
    graph = {i: set() for i in range(n)}

    for i in range(n):
        for j in range(n):
            if adj[i][j] and i != j:
                graph[i].add(j)
                graph[j].add(i)
            elif i == j and adj[i][j] == True:
                return False

    visited, candidates = [], []
    for n in graph.keys():
        visited, candi = dfs(graph=graph,
                             node=n,
                             visited=visited,
                             candidates=[])
        if candi:
            candidates += [candi]

    if candidates:
        if len(candidates) > 1: return False
        for candi in candidates:
            con_list = [len(graph[n]) for n in candi]
            cc = max(con_list)
            rest = [cn for cn in con_list if cn != cc]
            if list(set(con_list)) == [3] and len(con_list) == 4:
                return True
            if len(con_list) == cc + 1 and list(set(rest)) == [3]:
                return True

    return False


def dfs(graph, node, visited, candidates):
    if node not in visited:
        visited.append(node)
        candidates.append(node)
        if graph[node]:
            for n in graph[node]:
                visited, candidates = dfs(graph=graph,
                                          node=n,
                                          visited=visited,
                                          candidates=candidates)
    return visited, candidates



