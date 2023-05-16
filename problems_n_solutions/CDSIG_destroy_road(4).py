def solution(roadRegister):
    new_roadRegister = []
    cities = len(roadRegister)

    for city in range(cities):
        roads = []
        # city - target to be destroyed
        for i, row in enumerate(roadRegister):
            if i == city: continue
            new_road = []
            for j, col in enumerate(row):
                if j == city: continue
                new_road += [col]
            roads += [new_road]

        new_roadRegister += [roads]

    return new_roadRegister