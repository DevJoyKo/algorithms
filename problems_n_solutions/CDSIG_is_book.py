def solution(adj):
    n = len(adj)
    graph = {i: set() for i in range(n)}

    for i in range(n):
        for j in range(n):
            if adj[i][j] == True:
                graph[i].add(j)
                graph[j].add(i)

    max_cnt = max([len(v) for k, v in graph.items()])
    base_node = []
    print(max_cnt)

    for node in graph.keys():
        if len(graph[node]) == max_cnt:
            base_node += [node]

    if len(base_node) != 2 and not (len(base_node) == 3 and n == 3):
        return False

    base_left, base_right = graph[base_node[0]], graph[base_node[1]]

    if n > 2:
        if n == 3:
            for i in range(n):
                if not list(graph[i]) == list(set(graph.keys()) - set([i])):
                    return False
        else:
            for node in base_left:
                if node == base_node[1]: continue
                if not graph[node] == set(base_node):
                    return False
            for node in base_right:
                if node == base_node[0]: continue
                if not graph[node] == set(base_node):
                    return False
    elif n == 2:
        if not (graph[0] == set([1]) and graph[1] == set([0])):
            return False
    return True


def solution2(adj):
    return not isSelfConnecting(adj) and solutionSignature(adj)


def isSelfConnecting(adj):
    #any() : 하나라도 True인게 있으면 True
    #all() : 모두 True여야 True 반환
    return any(adj[i][i] for i in range(len(adj)))


def solutionSignature(adj):
    # boolen count: True 값 count
    return sorted(sum(row) for row in adj) == [2] * (len(adj) - 2) + [len(adj) - 1] * 2



