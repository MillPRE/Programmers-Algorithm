# https://school.programmers.co.kr/learn/courses/30/lessons/181928

def solution(num_list):
    answer = 0
    odd = ''
    even = ''

    for n in num_list:
        if n % 2 == 0:
            even += str(n)
        else:
            odd += str(n)

    return int(even) + int(odd)
