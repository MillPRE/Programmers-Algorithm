# https://school.programmers.co.kr/learn/courses/30/lessons/181902

def solution(my_string):
    answer = [0 for i in range(52)]
    # 0 ~ 25: A ~ Z
    # 26 ~ 52: a ~ z
    # A ~ Z: 65 ~ 90
    # a ~ z: 97 ~ 122

    for s in my_string:
        if ord(s) <= 90:
            answer[ord(s)%65] += 1
        else:
            answer[ord(s)%97 + 26] += 1

    return answer
