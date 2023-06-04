def solution(adj):
    n = len(adj)

    graph = {i: set() for i in range(n)}

    for i in range(n):
        for j in range(n):
            if i == j and adj[i][j] == True:
                return False
            if adj[i][j] == True:
                graph[i].add(j)
                graph[j].add(i)

    more_than_1 = [k for k, v in graph.items() if len(v) > 1]

    if len(more_than_1) < 3:
        return False

    adj_counts = [len(v) for k, v in graph.items()]
    max_nodes = [i for i in range(n) if len(graph[i]) == max(adj_counts)]

    triangle_candidates = set()

    for max_node in max_nodes:
        for node in graph[max_node]:
            if len(graph[node]) >= 2:
                triangle_candidates.add(node)
    triangle_candidates = list(triangle_candidates)

    new_candidates = []
    for node in triangle_candidates:
        if set(graph[node]) - set(triangle_candidates + max_nodes) and len(graph[node]) < 3:
            continue
        else:
            new_candidates += [node]

    triangles = set(max_nodes + new_candidates)
    if len(triangles) != 3:
        return False

    for triangle in triangles:
        if len(graph[triangle]) < 3 and set(graph[triangle]) - triangles:
            return False

    visited = []
    visited = dfs(node=0, graph=graph, visited=visited)
    if set(visited) != set(graph.keys()):
        return False

    return True


def dfs(node, graph, visited):
    if node not in visited:
        visited += [node]
        for nd in graph[node]:
            visited = dfs(node=nd, graph=graph, visited=visited)
    return visited


#TODO check
def solution2(adj):
    degseq = list(map(sum, adj))

    if sorted(degseq) in [[1, 1, 2, 2, 4], [1, 1, 2, 3, 3]]:
        # These degree sequences are unique up to isomorphism.
        return True

    elif sorted(degseq) == [1, 2, 2, 2, 3]:
        # There are two graphs on this degree sequence. In the graph
        # we want, all vertices of degree 2 are adjacent to the vertex
        # of degree 3.
        i = degseq.index(3)
        return all(row[i] for row in adj if sum(row) == 2)

    return False