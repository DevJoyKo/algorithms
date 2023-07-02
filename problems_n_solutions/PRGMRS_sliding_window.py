def solution(sequence, k):
    # sliding window problem
    # find the start, end index -> satisfies cumulative sum to be k
    start, end = 0, 0
    current_sum = sequence[0]
    min_length = float('inf') # length max로 잡아두기
    result = [0, 0] #

    while end < len(sequence): # 끝 index가 마지막 될 때까지
        if current_sum == k and (end - start + 1) < min_length:
            min_length = end - start + 1
            result = [start, end]
        if current_sum < k:
            end += 1
            if end < len(sequence):
                current_sum += sequence[end]
        else:
            current_sum -= sequence[start]
            start += 1
    return result


if __name__ == "__main__":
    answer = solution(sequence=[1,2,3,4,5], k=7)
    print(answer)
    assert answer == [2,3]



