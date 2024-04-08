def solution(number, k):
    stack = []
    for n in number:
        if len(stack) == 0:
            stack.append(n)
        else:
            while True:
                if len(stack) == 0 or k == 0:
                    break
                if stack[-1] >= n:
                    break
                if stack[-1] < n and k > 0:
                    stack.pop()
                    k -= 1
            stack.append(n)

    if k > 0:
        while k > 0 :
            _min = min(stack)
            stack.remove(_min)
            k -= 1

    return "".join(stack)

numbers = [
    "1924",
    "1231234",
    "4177252841",
    "4321",
    "43211",
    "8156298",
    "190000002",
    "909090",
    "053231238539",
    "5050505222",
    "1234567890123456789012345678901234567890",
    "928857",
    "99991",
    "10001"
]

ks = [
    2,
    3,
    4,
    2,
    3,
    3,
    3,
    2,
    5,
    3,
    1,
    3,
    3,
    3
]

results = [
    "94",
    "3234",
    "775841",
    "43",
    "43",
    "8698",
    "900002",
    "9990",
    "5338539",
    "5555222",
    '234567890123456789012345678901234567890',
    "988",
    "99",
    "11"
]

for idx in range(len(numbers)):
    print(f'test_case #{idx}: {numbers[idx]}')
    number = numbers[idx]
    k = ks[idx]
    answer = solution(number, k)
    print(f'return answer: {answer}, real_answer: {results[idx]}')
    print(f'{"PASS" if answer == results[idx] else "FAIL"}\n')