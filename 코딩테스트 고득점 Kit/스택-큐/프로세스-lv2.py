def solution(priorities, location):
    answer = []

    priorities = [[priorities[idx], idx] for idx in range(len(priorities))]

    idx = 0
    while len(priorities) > 0:
        a = list(filter(lambda x: x[0] > priorities[idx][0], priorities))
        # print(priorities[idx][0], len(a), priorities)
        if len(a) > 0:
            tmp = priorities.pop(0)
            priorities.append(tmp)
        if len(a) == 0:
            answer.append(priorities[idx])
            priorities.pop(0)

    for idx in range(len(answer)):
        if answer[idx][1] == location:
            return idx+1
