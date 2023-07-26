def solution(a, b, c):
    answer = 0

    data = set([a,b,c])
    data = list(data)

    if len(data) == 3:
        return a+b+c
    elif len(data) == 2:
        return (a+b+c) * (a*a + b*b + c*c)
    else:
        return (a+b+c) * (a*a + b*b + c*c) * (a*a*a + b*b*b + c*c*c)
