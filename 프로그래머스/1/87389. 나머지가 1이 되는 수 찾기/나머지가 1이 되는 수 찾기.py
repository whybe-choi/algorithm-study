def solution(n):
    answer =  [x for x in range(1, n+1) if n % x == 1][0]
    return answer