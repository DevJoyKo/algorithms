def solution(roadRegister):
    road_before = {}

    for row_index, row in enumerate(roadRegister):
        road_before[row_index] = [j for j, connect in enumerate(row) if connect == True]

    road_after = {}

    for node in road_before.keys():
        if node == len(roadRegister) - 1:
            new_id = 0
        else:
            new_id = node + 1
        road_after[new_id] = []
        for connect in road_before[node]:
            if connect != len(roadRegister) - 1:
                new_item_id = connect + 1
            else:
                new_item_id = 0
            road_after[new_id] += [new_item_id]

    new_roadRegister = []

    for num, _ in enumerate(roadRegister):
        num_road = []
        for j in range(len(roadRegister)):
            if j in road_after[num]:
                num_road += [True]
            else:
                num_road += [False]

        new_roadRegister.append(num_road)
    return new_roadRegister

def solution2(roadRegister):
    swap = lambda x: [x[-1]] + x[:-1]
    return swap([swap(road) for road in roadRegister])

if __name__ == "__main__":
    sample = [[False,True,True,False],
             [True,False,True,False],
             [True,True,False,True],
             [False,False,True,False]]
    res = solution(sample)
    res2 = solution2(sample)
    print(res)
    print(res2)