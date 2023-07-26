# https://school.programmers.co.kr/learn/courses/30/lessons/181847

def solution(n_str):
    while n_str[0] == '0':
        n_str = n_str[1:]

    return n_str
