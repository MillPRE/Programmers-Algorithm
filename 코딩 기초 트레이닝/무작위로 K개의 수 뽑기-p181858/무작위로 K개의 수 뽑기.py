# https://school.programmers.co.kr/learn/courses/30/lessons/181858

 def solution(arr, k):
     answer = []

     for a in arr:
         if not a in answer:
             answer.append(a)

         if len(answer) == k:
             break

     if len(answer) < k:
         while len(answer) < k:
             answer.append(-1)

     return answer
