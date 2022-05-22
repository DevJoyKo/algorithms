# -*- coding: utf-8 -*-

def linear_search(element, some_list):

    for idx, item in enumerate(some_list):
        if item == element:
            return idx
    return None


def test():
    answer_lists = [0, None, 2, 1, 4]
    result_lists = []
    test_case1 = linear_search(2, [2, 3, 5, 7, 11])
    test_case2 = linear_search(0, [2, 3, 5, 7, 11])
    test_case3 = linear_search(0, [2, 3, 5, 7, 11])
    test_case4 = linear_search(5, [2, 3, 5, 7, 11])
    test_case5 = linear_search(5, [2, 3, 5, 7, 11])
    test_case6 = linear_search(3, [2, 3, 5, 7, 11])
    test_case7 = linear_search(11, [2, 3, 5, 7, 11])

    result_lists += [test_case1,
                     test_case2,
                     test_case3,
                     test_case4,
                     test_case5,
                     test_case6,
                     test_case7]

    if answer_lists == result_lists:
        return "SUCCESS"
    else:
        return "FAIL"


if __name__ == "__main__":
    test_result = test()
    if test_result == "SUCCESS":
        print('{} 테스트 통과!'.format(linear_search.__name__))
    else:
        print('{} 테스트 실패!'.format(linear_search.__name__))