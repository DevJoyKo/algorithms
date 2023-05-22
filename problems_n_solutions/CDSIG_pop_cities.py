def solution(n, roads):
    all_nodes = []

    graph = {}

    for road in roads:
        if road[0] in graph.keys():
            graph[road[0]] += [road[1]]
        else:
            graph[road[0]] = [road[1]]

        if road[1] in graph.keys():
            graph[road[1]] += [road[0]]
        else:
            graph[road[1]] = [road[0]]
        all_nodes += [road[0], road[1]]

    iteration = 0
    node_iter = {}
    nodes_all = range(n)

    for nd in nodes_all:
        if nd not in graph.keys():
            graph[nd] = []

    del_list = []
    del_list, iteration, node_iter = pop_nodes(graph, del_list, iteration, node_iter)

    new = []

    for i in range(len(nodes_all)):
        if i in node_iter.keys():
            new += [node_iter[i]]
        else:
            new += [-1]

    return new


def pop_nodes(graph, del_list, iteration, node_iter):
    iteration += 1
    new_del_list = [*del_list]
    check_flag = False

    for node in graph.keys():
        if node in del_list: continue
        adjacents = [nd for nd in graph[node] if nd not in del_list]

        if len(adjacents) <= 1 or not graph[node]:
            check_flag = True
            node_iter[node] = iteration
            new_del_list += [node]

    if check_flag:
        pop_nodes(graph, new_del_list, iteration, node_iter)

    return del_list, iteration, node_iter