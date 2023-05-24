def solution(roadRegister):
    pairs = []
    for i, _ in enumerate(roadRegister):
        for j, tf in enumerate(roadRegister[i]):
            if tf == True:
                item = set([i, j])
                if item not in pairs:
                    pairs.append(item)

    new_road = []

    for i, (s1, e1) in enumerate(pairs):
        road = []
        for j, (s2, e2) in enumerate(pairs):
            if i == j:
                flag = False
            elif s1 in (s2, e2) or e1 in (s2, e2):
                flag = True
            else:
                flag = False
            road += [flag]
        new_road += [road]

    return new_road

# compair point -> enumerate vs range
# 행렬문제 풀때는 range + 행렬 정보 쓰는게 보다 깔끔한듯!

def solution2(roadRegister):
    n = len(roadRegister)

    roads = []
    for i in range(n):
        for j in range(i + 1, n):
            if roadRegister[i][j]:
                roads.append((i, j))

    m = len(roads)
    newRegister = [[False] * m for _ in range(m)]
    for i in range(m):
        for j in range(i + 1, m):
            if set(roads[i]) & set(roads[j]):
                newRegister[i][j] = True
                newRegister[j][i] = True

    return newRegister
