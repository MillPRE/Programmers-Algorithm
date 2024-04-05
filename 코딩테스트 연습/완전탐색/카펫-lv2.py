def solution(brown, yellow):
    brown -= 4
    brown = brown // 2

    for i in range(1, brown):
        if i * (brown - i) == yellow:
            answer = [i + 2, brown - i + 2]
            answer.sort(reverse=True)
            return answer