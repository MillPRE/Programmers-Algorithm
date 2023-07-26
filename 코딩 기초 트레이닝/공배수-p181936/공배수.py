def solution(number, n, m):
    return 0 if number % n + number % m > 0 else 1
