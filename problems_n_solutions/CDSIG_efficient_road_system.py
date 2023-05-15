from itertools import combinations

INF = int(1e9)

# CDSIG efficient road algorithms
# TODO better data structure usage
def solution(n, roads):
    if n <= 1:
        return True

    graph = [[] for i in range(n)]

    sorted_roads = [sorted(road) for road in roads]
    sorted_roads += [sorted(road, reverse=True) for road in roads]

    for i, road in enumerate(sorted_roads):
        graph[road[0]] += [road[1]]

    distances = [[0] * n for _ in range(n)]

    combis = combinations(range(n), 2)

    for combi in combis:

        start, end = combi
        distances[start][end] = -1
        distances[end][start] = -1

        if end in graph[start]:
            distance = 1
            distances[start][end] = distance
            distances[end][start] = distance
            continue

        for i in graph[start]:
            if end in graph[i]:
                distance = 2
                distances[start][end] = distance
                distances[end][start] = distance

    all_dists = []

    for dist in distances:
        all_dists += dist

    filter_over_2 = [i for i in all_dists if i < 0]

    if filter_over_2: return False

    return True