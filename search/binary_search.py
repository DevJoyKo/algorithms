def binary_search(element, some_list):

    start_index = 0
    end_index = len(some_list) - 1

    while start_index <= end_index:
        mid_index = (start_index + end_index) // 2
        if some_list[mid_index] == element:
            return mid_index
        elif some_list[mid_index] < element:
            start_index = mid_index + 1
        else:
            end_index = mid_index - 1
    return None

def test():
    answer_lists = [0, None, 2, 1, 4]
    result_lists = []
    test_case1 = binary_search(2, [2, 3, 5, 7, 11])
    test_case2 = binary_search(0, [2, 3, 5, 7, 11])
    test_case3 = binary_search(5, [2, 3, 5, 7, 11])
    test_case4 = binary_search(3, [2, 3, 5, 7, 11])
    test_case5 = binary_search(11, [2, 3, 5, 7, 11])

    result_lists += [test_case1,
                     test_case2,
                     test_case3,
                     test_case4,
                     test_case5]

    if answer_lists == result_lists:
        return "SUCCESS"
    else:
        return "FAIL"

if __name__ == "__main__":
    test_result = test()
    if test_result == "SUCCESS":
        print('{} 테스트 통과!'.format(binary_search.__name__))
    else:
        print('{} 테스트 실패!'.format(binary_search.__name__))