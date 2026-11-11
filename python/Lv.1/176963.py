# 추억 점수

import sys

name = list(sys.stdin.readline().split())
yearning = list(map(int, sys.stdin.readline().split()))
photo = list(sys.stdin.readline().split())

def solution(name, yearning, photo):
    answer = []

    for x in range(len(photo)) :
        answer.append(0)
    
    for i in range(len(photo)) :
        for k in range(len(name)) :
            if name[k] in photo[i] : answer[i] += yearning[k]

    return answer

print(solution(name, yearning, photo))