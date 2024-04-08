import copy
def solution(n, lost, reserve):
    lost.sort()
    temp = copy.deepcopy(lost)

    for idx in range(len(lost)):
        if lost[idx] in reserve:
            temp.remove(lost[idx])
            reserve.remove(lost[idx])

    lost = copy.deepcopy(temp)

    for l in lost:
        if l-1 in reserve:
            temp.remove(l)
            reserve.remove(l-1)
        elif l+1 in reserve:
            temp.remove(l)
            reserve.remove(l+1)

    return n - len(temp)


test_case = [
    [5, [2,4], [1,3,5]],
    [5, [2,4], [3]],
    [3, [3], [1]],
    [5, [2,3], [3,4]]
]

result = [
    5,
    4,
    2,
    4
]

for idx in range(len(test_case)):
    print(f'test_case #{idx}: {test_case[idx]}')
    n, lost, reserve = test_case[idx][0], test_case[idx][1], test_case[idx][2]
    answer = solution(n, lost, reserve)
    print(f'return answer: {answer}, real_answer: {result[idx]}')
    print(f'{"PASS" if answer == result[idx] else "FAIL"}\n')
