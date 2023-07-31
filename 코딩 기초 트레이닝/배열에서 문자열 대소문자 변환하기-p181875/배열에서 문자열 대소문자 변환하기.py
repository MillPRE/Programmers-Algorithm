# https://school.programmers.co.kr/learn/courses/30/lessons/181875

def solution(strArr):
    # 홀수 인덱스 대문자
    # 짝수 인덱스 소문자

    answer = []

    for index, s in enumerate(strArr):
        if index % 2 == 0 :
            answer.append(s.lower())
        else:
            answer.append(s.upper())

    return answer
