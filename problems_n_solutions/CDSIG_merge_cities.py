import numpy as np

# TODO & 분석
def solution(reg):
    num, city2merge, reg = len(reg), [], np.array(reg)
    # print(num - num % 2)
    # for i in range(0, num - num % 2, 2):
        # print(i)

    for c1, c2 in ((i, i + 1) for i in range(0, num - num % 2, 2)):
        if reg[c1][c2]:
            city2merge.append(c2)
            reg[c1][c2] = reg[c2][c1] = False
            reg[c1] |= reg[c2]
            reg[:, c1] |= reg[:, c2]
    reg = np.delete(reg, city2merge, 0)
    reg = np.delete(reg, city2merge, 1)

    return reg

solution([
  [False, True,  True,  False, False, False, True],
  [True,  False, True,  False, True,  False, False],
  [True,  True,  False, True,  False, False, True],
  [False, False, True,  False, False, True,  True],
  [False, True,  False, False, False, False, False],
  [False, False, False, True,  False, False, False],
  [True,  False, True,  True,  False, False, False]
])