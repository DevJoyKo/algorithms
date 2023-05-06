import time

# message commit test
def main(hour):
    """
        return cases of '3' occurrence - using collections
    """
    start = time.time()
    hour_wo_3_counts = 0
    min_wo_3_cases = 0
    sec_wo_3_cases = 0

    for i in range(0, hour+1):
        if '3' not in str(i):
            hour_wo_3_counts += 1

    for i in range(0, 60):
        if '3' not in str(i):
            min_wo_3_cases += 1
            sec_wo_3_cases += 1

    end = time.time()
    answer = (hour+1)*60*60 - (hour_wo_3_counts*min_wo_3_cases*sec_wo_3_cases)
    print(f"{(end - start) * 1000}ms")
    return answer

def main2(hour):
    """
    return cases of '3' occurrence - Brute Force
    """
    start = time.time()

    case_count = 0
    for i in range(hour+1):
        for j in range(60):
            for k in range(60):
                check_str = f'{i}{j}{k}'
                if '3' in check_str:
                    case_count += 1
    end = time.time()
    print(f"{(end-start)*1000}ms")
    return case_count


if __name__ == "__main__":
    res1 = main(5)
    res = main2(5)
    print(res1, res)