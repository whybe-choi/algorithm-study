def solution(sides):
    answer = 1 if sorted(sides)[2] < sorted(sides)[0] + sorted(sides)[1] else 2
    return answer