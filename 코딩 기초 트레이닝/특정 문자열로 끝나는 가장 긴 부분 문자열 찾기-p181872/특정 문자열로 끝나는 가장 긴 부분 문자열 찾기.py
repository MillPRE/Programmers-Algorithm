# https://school.programmers.co.kr/learn/courses/30/lessons/181872

def solution(myString, pat):
    idx = myString.rindex(pat)

    return myString[0: idx+len(pat)]
