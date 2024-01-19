def solution(n, words):
    p = [[] for _ in range(n)]
    say = []

    idx = 0
    for w in words:
        if idx == n:
            idx = 0
        p[idx].append(w)
        idx += 1

    times = 1
    prev = ''
    for time in range(len(p[0])):
        for i in range(len(p)):
            # print(prev, p[i][time])
            if prev == '':
                prev = p[i][time]
                pass
            elif time < len(p[i]) and prev[-1] != p[i][time][0]:
                return [i + 1, time + 1]
            elif p[i][time] in say:
                return [i + 1, time + 1]
            say.append(prev)
            prev = p[i][time]

    return [0, 0]