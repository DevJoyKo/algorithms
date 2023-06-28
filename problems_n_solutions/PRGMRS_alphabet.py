import time
def solution(s, skip, index):
    answer = ''
    alphabets = list("abcdefghijklmnopqrstuvwxyz")
    cnt_alpha = len(alphabets)

    for character in list(s):
        current_index = alphabets.index(character)
        skip_cnt = 0

        i = current_index + 1

        while True:
            if alphabets[i % cnt_alpha] not in skip:
                skip_cnt += 1
            if skip_cnt == index: break
            i += 1

        answer = answer + alphabets[i%cnt_alpha]
    return answer


def solution2(s, skip, index):
    from string import ascii_lowercase

    result = ''

    a_to_z = set(ascii_lowercase)
    a_to_z -= set(skip)
    a_to_z = sorted(a_to_z)
    l = len(a_to_z)

    dic_alpha = {alpha: idx for idx, alpha in enumerate(a_to_z)}

    for i in s:
        result += a_to_z[(dic_alpha[i] + index) % l]

    return result


if __name__ == "__main__":
    start = time.time()
    res = solution(s="aukks", skip="wbqd", index=5)
    end = time.time()
    print(res, (end-start)*1000)
    assert res == "happy"

    start2 = time.time()
    res2 = solution2(s="aukks", skip="wbqd", index=5)
    end2 = time.time()
    print(res2, (end-start)*1000)
    assert res2 == "happy"

