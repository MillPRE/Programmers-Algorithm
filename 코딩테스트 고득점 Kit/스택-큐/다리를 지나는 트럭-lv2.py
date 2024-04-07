from collections import deque


def solution(bridge_length, weight, truck_weights):
    max_count = bridge_length
    max_weight = weight

    time = 0
    n = len(truck_weights)

    Complete = deque()
    Progress = deque()
    Wait = deque(truck_weights)

    while len(Complete) < n:
        time += 1
        if len(Progress) > 0:
            for idx in range(len(Progress)):
                Progress[idx][0] -= 1
            if Progress[0][0] == 0:
                Complete.append(Progress.popleft())

        if len(Wait) > 0:
            _sum = sum(sub_arr[1] for sub_arr in Progress)
            if len(Progress) < max_count and _sum + Wait[0] <= max_weight:
                Progress.append([max_count, Wait.popleft()])

    return time