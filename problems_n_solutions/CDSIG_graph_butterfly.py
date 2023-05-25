import numpy as np

def solution(adj):
    n = len(adj)

    adj_nodes = []

    for i in range(n):
        for j in range(n):
            if i == j and adj[i][j] == True:
                return False
            if adj[i][j] == True:
                adj_nodes += [i, j]

    unique, counts = np.unique(adj_nodes, return_counts=True)
    unique_dict = dict(zip(unique, counts))

    vs = list(unique_dict.values())

    if vs.count(8) == 1 and vs.count(4) == 4:
        return True
    return False