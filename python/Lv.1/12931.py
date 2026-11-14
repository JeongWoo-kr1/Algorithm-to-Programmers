# 자릿수 더하기

import sys

n = sys.stdin.readline().strip()

def solution(n):
    answer = 0
    for i in range(len(str(n))):
        answer += int(str(n)[i])

    return answer

print(solution(n))