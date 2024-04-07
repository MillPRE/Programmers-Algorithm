def solution(citations):
    answer = 0
    n = len(citations)
    _max = max(citations)

    for h in range(_max):
        cnt = 0
        for c in citations:
            if c >= h:
                cnt += 1
        if cnt >= h:
            answer = h
    return answer