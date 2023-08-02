# https://school.programmers.co.kr/learn/courses/30/lessons/181865

def solution(binomial):
    answer = 0

    binomial = list(binomial.strip().split(" "))
    a = int(binomial[0])
    op = binomial[1]
    b = int(binomial[2])

    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    else:
        return a * b
