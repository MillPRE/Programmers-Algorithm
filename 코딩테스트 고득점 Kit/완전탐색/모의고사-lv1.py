def solution(answers):
    answer = [0, 0, 0]
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    aIdx = 0  # 5가 되면 aIdx = 0
    bIdx = 0  # 8이 되면 bIdx = 0
    cIdx = 0  # 10이 되면 cIdx = 0

    for ans in answers:
        if aIdx == 5:
            aIdx = 0
        if bIdx == 8:
            bIdx = 0
        if cIdx == 10:
            cIdx = 0

        if a[aIdx] == ans:
            answer[0] += 1
        if b[bIdx] == ans:
            answer[1] += 1
        if c[cIdx] == ans:
            answer[2] += 1
        aIdx += 1
        bIdx += 1
        cIdx += 1

    _max = max(answer)
    result = []

    for i in range(len(answer)):
        if _max == answer[i]:
            result.append(i + 1)
    return result