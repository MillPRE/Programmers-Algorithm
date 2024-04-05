from itertools import permutations as p

def solution(k, dungeons):
    answer = -1
    m = 0
    l = len(dungeons)
    for o in p(range(l)):
        hp = k
        cnt = 0
        for n, i in enumerate(o):
            if hp >= dungeons[i][0]:
                cnt += 1
                hp -= dungeons[i][1]
        if cnt > answer:
            answer = cnt
    return answer