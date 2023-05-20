def solution(roads):
    graph = {}
    for road in roads:
        if road[0] in graph:
            graph[road[0]] += [road[2]]
        else:
            graph[road[0]] = [road[2]]
        if road[1] in graph:
            graph[road[1]] += [road[2]]
        else:
            graph[road[1]] = [road[2]]

    for node in graph.keys():
        adjacents = sorted(graph[node])
        for index, adjacent in enumerate(adjacents[:-1]):
            if abs(adjacents[index] - adjacents[index+1]) <= 1:
                return False
    return True