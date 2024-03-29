def solution1(n, roads):
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
    del_list, iteration, node_iter = pop_nodes1(graph, del_list, iteration, node_iter)

    new = []

    for i in range(len(nodes_all)):
        if i in node_iter.keys():
            new += [node_iter[i]]
        else:
            new += [-1]

    return new


def pop_nodes1(graph, del_list, iteration, node_iter):
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
        pop_nodes1(graph, new_del_list, iteration, node_iter)

    return del_list, iteration, node_iter


def solution2(n, roads):
    graph = {nd: set() for nd in range(n)}
    conquer = [-1 for _ in range(n)]

    for road in roads:
        graph[road[0]].add(road[1])
        graph[road[1]].add(road[0])

    days = 0
    node_iter = {}
    conquer_cities = []

    conquer_cities, days, node_iter = pop_nodes2(graph, conquer_cities, days, node_iter)

    for i in range(n):
        if i in node_iter.keys():
            conquer[i] = node_iter[i]
    return conquer


def pop_nodes2(graph, conquer_cities, days, node_iter):
    days += 1
    new_del_list = [*conquer_cities]
    check_flag = False

    for node in graph.keys():
        if node in conquer_cities: continue
        adjacents = [nd for nd in graph[node] if nd not in conquer_cities]

        if len(adjacents) <= 1 or not graph[node]:
            check_flag = True
            node_iter[node] = days
            new_del_list += [node]

    if check_flag:
        pop_nodes2(graph, new_del_list, days, node_iter)

    return conquer_cities, days, node_iter

if __name__ == "__main__":
    roads = [[1, 0], [1, 2], [8, 5], [9, 7], [5, 6], [5, 4], [4, 6], [6, 7]]
    print(solution1(10, roads))
    print(solution2(10, roads))