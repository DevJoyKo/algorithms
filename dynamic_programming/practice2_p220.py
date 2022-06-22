rooms = int(input())

foods = [0]

for i in range(rooms):
    foods += [int(input())]

# print(foods)
counts = [0] * 101

for i in range(3, rooms+1):
    print(i)
    if i == 3:
        counts[i] = max(foods[1] + foods[3], foods[2])
    elif i == 4:
        counts[i] = max(foods[2] + foods[4], foods[1] + foods[3])
    else:
        counts[i] = max(counts[i-2] + foods[i], counts[i-1])
    # print(counts[i])

print(counts[rooms])