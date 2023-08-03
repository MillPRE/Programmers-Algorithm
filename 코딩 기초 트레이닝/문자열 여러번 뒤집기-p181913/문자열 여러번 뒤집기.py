# https://school.programmers.co.kr/learn/courses/30/lessons/181913

def solution(my_string, queries):
    for query in queries:
        s = query[0]
        e = query[1]

        a = my_string[:s]
        b = my_string[s:e+1][::-1]
        c = my_string[e+1:]

        my_string = a + b + c

    return my_string
