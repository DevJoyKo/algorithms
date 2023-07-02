def solution(plans):
    # not perfect code
    unfinished_stack = []
    finished_task = []

    dt_time = lambda x: int(x[0]) * 60 + int(x[1])
    plans = [
        [plan[0], dt_time(plan[1].split(":")), int(plan[2])]
        for plan in plans
    ]
    plans = sorted(plans, key=lambda y: y[1])

    # print(plans)
    for plan in plans:
        if not unfinished_stack:
            unfinished_stack.append(plan)
        else:
            recent_task = unfinished_stack.pop()
            recent_time = recent_task[1]
            current_time = plan[1]
            interval = current_time - recent_time

            duration = interval - recent_task[-1]

            if duration < 0:
                recent_task[-1] = abs(duration)
                unfinished_stack.append(recent_task)
                unfinished_stack.append(plan)
            else:
                finished_task.append(recent_task[0])
                unfinished_stack, finished_task = task_proceed_until_interval(unfinished_stack, duration, finished_task)
                unfinished_stack.append(plan)

    # after time slot finished
    for i in range(len(unfinished_stack)):
        finished_task.append(unfinished_stack.pop()[0])
    return finished_task


def task_proceed_until_interval(unfinished_stack,
                                interval_minutes,
                                finished_task):
    while int(interval_minutes) > 0 and unfinished_stack:
        recent_task = unfinished_stack.pop()
        duration = interval_minutes - recent_task[-1]
        interval_minutes = duration

        if duration >= 0:
            finished_task += [recent_task[0]]
        else:
            recent_task[-1] = abs(duration)
            unfinished_stack.append(recent_task)

    return unfinished_stack, finished_task


if __name__ == "__main__":
    plans = [["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]
    response = solution(plans=plans)
    print(response)
    assert response == ["korean", "english", "math"]